import random
# Fake DB
db = {
    "rasool@gmail.com": {"password": "1234", "type": "free"},
    "siri@gmail.com": {"password": "abcd", "type": "premium"}
}

songs_db = ["Shape of You", "Blinding Lights", "Believer", "Heat Waves", "Senorita"]

# ================= Base Class ===================
class Users:
    def __init__(self, email, password, user_type="free"):
        self.email = email
        self.__password = password
        self.user_type = user_type  # free/premium
        self.playlist = []
  
    def getpassword(self):
        return self.__password
    
    def upgrade_to_premium(self):
        if self.user_type == "free":
            self.user_type = "premium"
            print(f"{self.email} has been upgraded to Premium!")
        else:
            print(f"{self.email} is already a Premium user.")

    def add_to_playlist(self, song):
        if song in songs_db:
            self.playlist.append(song)
            print(f"{song} added to your playlist.")
        else:
            print("Song not found in DB.")
    
    def show_playlist(self):
        if not self.playlist:
            print("Your playlist is empty.")
        else:
            print(f"{self.email}'s Playlist: {self.playlist}")


# ================= Free User ===================
class FreeUser(Users):
    def feautures(self):
        print('\nFeatures of Free Users')
        print("✔ Can stream songs but with ads.")
        print("✔ Can skip limited songs (like 6 skips per hour).")
        print("✔ No offline downloads.")  

    def play_song(self, song):
        print("Playing Advertisement... [Ad playing..]")
        if song in songs_db:
            print(f"Now Playing (Free with Ads): {song}")
        else:
            print("Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("Playlist is empty. Add some songs first.")
            return
        print("Playing Advertisement before your song...")
        song = random.choice(self.playlist)
        print(f"Now Playing Random (Free with Ads): {song}")
 
# ================= Premium User ===================
class PremiumUser(Users):
    def feautures(self):
        print('\nFeatures of Premium Users')
        print("✔ No ads, unlimited skips.")
        print("✔ Can download songs for offline use.")
        print("✔ Higher audio quality.") 
        print("✔ Artists get more money when premium users listen.")

    def play_song(self, song):
        if song in songs_db:
            print(f"Now Playing (Premium): {song}")
        else:
            print("Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("Playlist is empty. Add some songs first.")
            return
        song = random.choice(self.playlist)
        print(f"Now Playing Random (Premium, No Ads): {song}")

# ================= Content User (Artist) ===================
class ContentUser(Users):
    def upload_song(self, song):
        if song not in songs_db:
            songs_db.append(song)
            print(f"{self.email} uploaded new song: {song}")
        else:
            print("Song already exists in DB.")
# ================= Menu ===================
class Menu:
    def __init__(self, database):
        self.db = database
        print("=== Welcome to Spotify Clone ===")
        self.start()

    def start(self):
        while True:  # keep menu running until exit
            print("\n1. New User (Sign Up)")
            print("2. Existing User (Login)")
            print("3. Exit")
            choice = input("Enter choice (1/2/3): ")

            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye! Thanks for using Spotify Clone.")
                break
            else:
                print("Invalid choice! Try again.")

    def signup(self):
        print("\n--- Sign Up ---")
        email = input("Enter your email: ")
        if email in self.db:
            print("User already exists! Please login instead.")
            return

        password = input("Enter your password: ")
        self.db[email] = {"password": password, "type": "free"}
        print(f"Account created successfully for {email} (Free User)")
        print("Current Users in DB:", self.db.keys())

    def login(self):
        print("\n--- Login ---")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.db and self.db[email]["password"] == password:
            user_type = self.db[email]["type"]

            if user_type == "free":
                user = FreeUser(email, password, "free")
            elif user_type == "premium":
                user = PremiumUser(email, password, "premium")
            else:
                user = ContentUser(email, password, "content")

            print(f"Welcome {email} ({user_type.capitalize()} User)")
            self.user_menu(user, email)

        else:
            print("Invalid email or password.")

    def user_menu(self, user, email):
        while True:
            print("\n--- User Menu ---")
            print("1. Show Features")
            print("2. View All Songs")
            print("3. Play a Song")
            print("4. Add Song to Playlist")
            print("5. Show Playlist")
            print("6. Play Random Song from Playlist")
            if isinstance(user, FreeUser):
                print("7. Upgrade to Premium")
            if isinstance(user, ContentUser):
                print("8. Upload Song")
            print("9. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                user.feautures()
            elif choice == "2":
                print("Songs in DB:", songs_db)
            elif choice == "3":
                song = input("Enter song name to play: ")
                user.play_song(song)
            elif choice == "4":
                song = input("Enter song name to add: ")
                user.add_to_playlist(song)
            elif choice == "5":
                user.show_playlist()
            elif choice == "6":
                user.play_random_from_playlist()
            elif choice == "7" and isinstance(user, FreeUser):
                user.upgrade_to_premium()
                self.db[email]["type"] = "premium"
                return
            elif choice == "8" and isinstance(user, ContentUser):
                song = input("Enter new song name: ")
                user.upload_song(song)
            elif choice == "9":
                print("Logged out.")
                break
            else:
                print("Invalid option.")


Menu(db)