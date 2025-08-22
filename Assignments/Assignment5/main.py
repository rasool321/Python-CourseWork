import random
from abc import ABC, abstractmethod
from data import db, songs_db   # importing backend data


# ================= Helper Functions =================
def song_exists(song):
    """Check if a song exists in songs_db (any artist)."""
    for artist, songs in songs_db.items():
        if song in songs:
            return True
    return False


def show_all_songs():
    """Display all songs grouped by artist."""
    print("\n🎶 Songs in Catalog:")
    for artist, songs in songs_db.items():
        print(f"\n-- {artist} --")
        for s in songs:
            print(f"   • {s}")


def add_song_to_artist(artist, song):
    """Add a new song to a specific artist in songs_db."""
    if artist not in songs_db:
        songs_db[artist] = []
    if song not in songs_db[artist]:
        songs_db[artist].append(song)
        print(f"✅ {song} uploaded under {artist}")
    else:
        print("⚠️ Song already exists in DB.")


# ================= Abstraction + Encapsulation =================
class User(ABC):
    def __init__(self, email, password, user_type="free"):
        self.email = email
        self.__password = password         # encapsulated
        self.user_type = user_type
        self.playlist = []

    def get_password(self):
        return self.__password

    def add_to_playlist(self, song):
        if song_exists(song):
            self.playlist.append(song)
            print(f"{song} added to your playlist.")
        else:
            print("Song not found in DB.")

    def show_playlist(self):
        if not self.playlist:
            print("Your playlist is empty.")
        else:
            print(f"{self.email}'s Playlist: {self.playlist}")

    def upgrade_to_premium(self):
        if self.user_type == "free":
            self.user_type = "premium"
            print(f"{self.email} has been upgraded to Premium!")
        else:
            print(f"{self.email} is already Premium or Content.")

    @abstractmethod
    def features(self):
        pass

    @abstractmethod
    def play_song(self, song):
        pass

    @abstractmethod
    def play_random_from_playlist(self):
        pass


# ================= Inheritance + Polymorphism =================
class FreeUser(User):
    def features(self):
        print("\nFeatures of Free Users")
        print("• Stream with ads")
        print("• Limited skips")
        print("• No offline downloads")

    def play_song(self, song):
        print("Advertisement... [Ad playing]")
        if song_exists(song):
            print(f"Now Playing (Free w/ Ads): {song}")
        else:
            print("Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("Playlist is empty. Add some songs first.")
            return
        print("Advertisement before your song...")
        song = random.choice(self.playlist)
        print(f"Now Playing Random (Free w/ Ads): {song}")


class PremiumUser(User):
    def features(self):
        print("\nFeatures of Premium Users")
        print("• No ads, unlimited skips")
        print("• Offline downloads")
        print("• Higher audio quality")

    def play_song(self, song):
        if song_exists(song):
            print(f"Now Playing (Premium): {song}")
        else:
            print("Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("Playlist is empty. Add some songs first.")
            return
        song = random.choice(self.playlist)
        print(f"Now Playing Random (Premium, No Ads): {song}")


# Content user plays like a free user (ads) AND can upload.
class ContentUser(FreeUser):
    def __init__(self, email, password, user_type="content"):
        super().__init__(email, password, user_type)

    def features(self):
        print("\nFeatures of Content Users (Artist)")
        print("• Stream with ads (like Free)")
        print("• Create & manage playlists")
        print("• Upload new songs to the global catalog")

    def upload_song(self, artist, song):
        add_song_to_artist(artist, song)


# ===================== Menu / UI =====================
class Menu:
    def __init__(self, database):
        self.db = database
        print("=== Welcome to Spotify Clone ===")
        self.start()

    def start(self):
        while True:
            print("\n1) New User (Sign Up)")
            print("2) Existing User (Login)")
            print("3) Content User")
            print("4) Exit")
            choice = input("Enter choice (1/2/3/4): ").strip()

            if choice == "1":
                self.signup_regular()
            elif choice == "2":
                self.login_regular()
            elif choice == "3":
                self.content_portal()
            elif choice == "4":
                print("Goodbye! Thanks for using Spotify Clone.")
                break
            else:
                print("Invalid choice! Try again.")

    # ----- Regular users (free/premium) -----
    def signup_regular(self):
        print("\n--- Sign Up (Regular User) ---")
        email = input("Email: ").strip().lower()
        if email in self.db:
            print("User already exists! Please login instead.")
            return

        password = input("Password: ").strip()
        role = input("Choose account type (free/premium): ").strip().lower()
        if role not in {"free", "premium"}:
            print("Invalid type. Defaulting to FREE.")
            role = "free"

        self.db[email] = {"password": password, "type": role}
        print(f"Account created for {email} ({role.capitalize()} User)")

    def login_regular(self):
        print("\n--- Login (Existing User) ---")
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        if email in self.db and self.db[email]["password"] == password:
            user_type = self.db[email]["type"]
            if user_type == "free":
                user = FreeUser(email, password, "free")
            elif user_type == "premium":
                user = PremiumUser(email, password, "premium")
            elif user_type == "content":
                print("This is a Content account. Use 'Content User' from the main menu.")
                return
            else:
                print("Unknown user type in DB.")
                return

            print(f"Welcome {email} ({user_type.capitalize()} User)")
            self.user_menu(user, email)
        else:
            print("Invalid email or password.")

    # ----- Content users (separate portal) -----
    def content_portal(self):
        while True:
            print("\n--- Content User ---")
            print("1) Login as Content User")
            print("2) Sign Up as Content User")
            print("3) Back")
            ch = input("Enter choice (1/2/3): ").strip()
            if ch == "1":
                self.login_content()
                return
            elif ch == "2":
                self.signup_content()
            elif ch == "3":
                return
            else:
                print("Invalid choice.")

    def signup_content(self):
        print("\n--- Sign Up (Content User) ---")
        email = input("Email: ").strip().lower()
        if email in self.db:
            print("User already exists! Please login instead.")
            return
        password = input("Password: ").strip()
        self.db[email] = {"password": password, "type": "content"}
        print(f"Account created for {email} (Content User)")

    def login_content(self):
        print("\n--- Login (Content User) ---")
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        if email in self.db and self.db[email]["password"] == password:
            if self.db[email]["type"] != "content":
                print("Not a Content account. Use 'Existing User' to login.")
                return
            user = ContentUser(email, password, "content")
            print(f"Welcome {email} (Content User)")
            self.user_menu(user, email)
        else:
            print("Invalid email or password.")

    # ----- Shared user menu -----
    def user_menu(self, user, email):
        while True:
            print("\n--- User Menu ---")
            print("1) Show Features")
            print("2) View All Songs")
            print("3) Play a Song")
            print("4) Add Song to Playlist")
            print("5) Show Playlist")
            print("6) Play Random Song from Playlist")
            if isinstance(user, FreeUser) and not isinstance(user, ContentUser):
                print("7) Upgrade to Premium")
            if isinstance(user, ContentUser):
                print("8) Upload Song")
            print("9) Logout")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                user.features()
            elif choice == "2":
                show_all_songs()
            elif choice == "3":
                song = input("Enter song name to play: ").strip()
                user.play_song(song)
            elif choice == "4":
                song = input("Enter song name to add: ").strip()
                user.add_to_playlist(song)
            elif choice == "5":
                user.show_playlist()
            elif choice == "6":
                user.play_random_from_playlist()
            elif choice == "7" and isinstance(user, FreeUser) and not isinstance(user, ContentUser):
                user.upgrade_to_premium()
                self.db[email]["type"] = "premium"
                return
            elif choice == "8" and isinstance(user, ContentUser):
                artist = input("Enter artist name: ").strip()
                song = input("Enter new song name to upload: ").strip()
                user.upload_song(artist, song)
            elif choice == "9":
                print("Logged out.")
                break
            else:
                print("Invalid option.")


# Run App
if __name__ == "__main__":
    Menu(db)
