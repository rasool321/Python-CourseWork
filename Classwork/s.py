from abc import ABC, abstractmethod

# 1. Abstraction
class Content(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass


# 2. Inheritance + Polymorphism
class Song(Content):
    def play(self):
        print(f"Playing song 🎵 {self.title} ({self.duration} mins)")


class Podcast(Content):
    def play(self):
        print(f"Streaming podcast 🎙 {self.title} ({self.duration} mins)")


# 3. Encapsulation
class User:
    def __init__(self, name, email, premium=False):
        self.name = name
        self.__email = email        # private
        self.__premium = premium    # private

    def get_email(self):
        return self.__email

    def upgrade_to_premium(self):
        self.__premium = True
        print(f"{self.name} is now a premium member!")


# 4. Class Method (alternative constructor)
class PremiumUser(User):
    @classmethod
    def from_email_signup(cls, email):
        name = email.split("@")[0]  # simple name extraction
        return cls(name, email, premium=True)


# 5. Super() usage in inheritance
class Artist(User):
    def __init__(self, name, email, genre):
        super().__init__(name, email, premium=True)  # artist always premium
        self.genre = genre

    def upload_song(self, song):
        print(f"Artist {self.name} uploaded {song.title}!")


# --- Realtime simulation ---
if __name__ == "__main__":
    # Create users
    u1 = User("Rasool", "rasool@gmail.com")
    u2 = PremiumUser.from_email_signup("siri@example.com")

    # Encapsulation demo
    print(u1.get_email())
    u1.upgrade_to_premium()

    # Artist
    a1 = Artist("Arijit Singh", "arijit@music.com", "Bollywood")

    # Content
    s1 = Song("Kesariya", 4)
    p1 = Podcast("TechTalk", 30)

    # Polymorphism in action
    s1.play()
    p1.play()

    # Super() demo
    a1.upload_song(s1)
