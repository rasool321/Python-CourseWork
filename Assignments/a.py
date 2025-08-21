import json
import os
import random
from abc import ABC, abstractmethod

STORE_FILE = "spotify_clone_store.json"

# ---------- Persistence Layer ----------
def load_store():
    if os.path.exists(STORE_FILE):
        with open(STORE_FILE, "r") as f:
            return json.load(f)
    # default seed data
    return {
        "users": {
            "rasool@gmail.com": {"password": "1234", "type": "free", "playlist": [], "activity": []},
            "siri@gmail.com":   {"password": "abcd", "type": "premium", "playlist": [], "activity": []}
        },
        "songs_db": ["Shape of You", "Blinding Lights", "Believer", "Heat Waves", "Senorita"]
    }

def save_store(store):
    with open(STORE_FILE, "w") as f:
        json.dump(store, f, indent=2)

store = load_store()          # { "users": {...}, "songs_db": [...] }
db = store["users"]           # convenience alias
songs_db = store["songs_db"]  # convenience alias

# ---------- Abstraction (Base User) ----------
class UserBase(ABC):
    def __init__(self, email, password, user_type, playlist=None):
        self.email = email
        self._password = password
        self.user_type = user_type
        self.playlist = list(playlist or [])

    def getpassword(self):
        return self._password

    def add_to_playlist(self, song):
        if song in songs_db:
            self.playlist.append(song)
            print(f"🎶 {song} added to your playlist.")
            db[self.email]["playlist"] = self.playlist
            db[self.email]["activity"].append(f"Added to playlist: {song}")
            save_store(store)
        else:
            print("⚠ Song not found in DB.")

    def show_playlist(self):
        if not self.playlist:
            print("📂 Your playlist is empty.")
        else:
            print(f"📂 {self.email}'s Playlist:")
            for i, s in enumerate(self.playlist, 1):
                print(f"  {i}. {s}")

    def upgrade_to_premium(self):
        if self.user_type == "free":
            self.user_type = "premium"
            db[self.email]["type"] = "premium"
            db[self.email]["activity"].append("Upgraded to Premium")
            save_store(store)
            print(f"✅ {self.email} has been upgraded to Premium!")
        else:
            print("ℹ️ Already Premium.")

    @abstractmethod
    def feautures(self):
        ...

    @abstractmethod
    def play_song(self, song):
        ...

    @abstractmethod
    def play_random_from_playlist(self):
        ...

# ---------- Free User ----------
class FreeUser(UserBase):
    def __init__(self, email, password, playlist=None):
        super().__init__(email, password, "free", playlist)

    def feautures(self):
        print("\nFeatures of Free Users")
        print("✔ Can stream songs but with ads.")
        print("✔ Limited skips.")
        print("❌ No offline downloads.")

    def play_song(self, song):
        print("📢 Playing Advertisement... [Ad]")
        if song in songs_db:
            print(f"🎵 Now Playing (Free with Ads): {song}")
            db[self.email]["activity"].append(f"Played song (free): {song}")
            save_store(store)
        else:
            print("⚠ Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("📂 Playlist is empty. Add some songs first.")
            return
        print("📢 Playing Advertisement... [Ad]")
        song = random.choice(self.playlist)
        print(f"🎵 Now Playing Random (Free with Ads): {song}")
        db[self.email]["activity"].append(f"Played random (free): {song}")
        save_store(store)

# ---------- Premium User ----------
class PremiumUser(UserBase):
    def __init__(self, email, password, playlist=None):
        super().__init__(email, password, "premium", playlist)

    def feautures(self):
        print("\nFeatures of Premium Users")
        print("✔ No ads, unlimited skips.")
        print("✔ Offline downloads.")
        print("✔ Higher audio quality.")

    def play_song(self, song):
        if song in songs_db:
            print(f"🎵 Now Playing (Premium): {song}")
            db[self.email]["activity"].append(f"Played song (premium): {song}")
            save_store(store)
        else:
            print("⚠ Song not available!")

    def play_random_from_playlist(self):
        if not self.playlist:
            print("📂 Playlist is empty. Add some songs first.")
            return
        song = random.choice(self.playlist)
        print(f"🎵 Now Playing Random (Premium, No Ads): {song}")
        db[self.email]["activity"].append(f"Played random (premium): {song}")
        save_store(store)

# ---------- Content User (Artist) ----------
# Inherits Free behavior (ads etc.) + can upload songs
class ContentUser(FreeUser):
    def __init__(self, email, password, playlist=None):
        super().__init__(email, password, playlist)
        self.user_type = "content"  # label

    def feautures(self):
        print("\nFeatures of Content Users (Creator)")
        print("✔ Can play like Free user (ads).")
        print("✔ Can create playlists.")
        print("✔ Can upload/add songs to global library.")

    def upload_song(self, song):
        if not song.strip():
            print("⚠ Invalid song name.")
            return
        if song in songs_db:
            print("ℹ️ Song already exists in DB.")
            return
        songs_db.append(song)
        store["songs_db"] = songs_db
        db[self.email]["activity"].append(f"Uploaded song: {song}")
        save_store(store)
        print(f"🎤 {self.email} uploaded new song: {song}")

# ---------- Menu / App ----------
class Menu:
    def __init__(self):
        print("=== Welcome to Spotify Clone (OOPS) ===")
        self.start()

    def start(self):
        while True:
            print("\n1) Sign Up (Free)")
            print("2) Sign Up as Content Creator")
            print("3) Login (Free/Premium/Content)")
            print("4) Exit")
            ch = input("Enter choice: ").strip()

            if ch == "1":
                self.signup("free")
            elif ch == "2":
                self.signup("content")
            elif ch == "3":
                self.login()
            elif ch == "4":
                print("👋 Goodbye! Saving your data...")
                save_store(store)
                break
            else:
                print("⚠ Invalid choice!")

    def signup(self, acc_type):
        print("\n--- Sign Up ---")
        email = input("Email: ").strip()
        if email in db:
            print("⚠ User already exists. Please login.")
            return
        pwd = input("Password: ").strip()
        db[email] = {
            "password": pwd,
            "type": acc_type,
            "playlist": [],
            "activity": ["Signed up"]
        }
        save_store(store)
        print(f"✅ Account created for {email} ({acc_type.capitalize()} user)")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ").strip()
        pwd = input("Password: ").strip()

        if email in db and db[email]["password"] == pwd:
            u = db[email]
            user_type = u["type"]
            playlist = u.get("playlist", [])

            if user_type == "free":
                user = FreeUser(email, pwd, playlist)
            elif user_type == "premium":
                user = PremiumUser(email, pwd, playlist)
            elif user_type == "content":
                user = ContentUser(email, pwd, playlist)
            else:
                print("⚠ Unknown user type.")
                return

            print(f"✅ Welcome {email} ({user_type.capitalize()} User)")
            db[email]["activity"].append("Logged in")
            save_store(store)
            self.user_menu(user)
        else:
            print("❌ Invalid email or password.")

    def show_all_songs(self):
        print("\n🎶 Songs in DB:")
        for i, s in enumerate(songs_db, 1):
            print(f"  {i}. {s}")

    def user_menu(self, user: UserBase):
        while True:
            print("\n--- User Menu ---")
            print("1) Show Features")
            print("2) View All Songs")
            print("3) Play a Song")
            print("4) Add Song to My Playlist")
            print("5) Show My Playlist")
            print("6) Play Random from My Playlist")

            # Free can upgrade; Content can upload; Premium already premium
            if isinstance(user, FreeUser) and not isinstance(user, ContentUser):
                print("7) Upgrade to Premium")
            if isinstance(user, ContentUser):
                print("8) Upload Song to Global Library")
            print("9) Logout")

            ch = input("Choose: ").strip()

            if ch == "1":
                user.feautures()
            elif ch == "2":
                self.show_all_songs()
            elif ch == "3":
                song = input("Enter song name to play: ").strip()
                user.play_song(song)
            elif ch == "4":
                song = input("Enter song name to add: ").strip()
                user.add_to_playlist(song)
            elif ch == "5":
                user.show_playlist()
            elif ch == "6":
                user.play_random_from_playlist()
            elif ch == "7" and isinstance(user, FreeUser) and not isinstance(user, ContentUser):
                user.upgrade_to_premium()
                # swap live object to Premium for the rest of session
                user = PremiumUser(user.email, user.getpassword(), user.playlist)
            elif ch == "8" and isinstance(user, ContentUser):
                song = input("New song title: ").strip()
                user.upload_song(song)
            elif ch == "9":
                print("🚪 Logged out.")
                db[user.email]["activity"].append("Logged out")
                save_store(store)
                break
            else:
                print("⚠ Invalid option.")

# ---- Run App ----
if __name__ == "__main__":
    Menu()
