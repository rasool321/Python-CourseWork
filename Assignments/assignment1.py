# 🎵 Spotify-style Track Information System 🎵

# Task 1: Take Track Details (Product) as Input
track_id = int(input("Enter Track ID: "))
track_name = input("Enter Track Name: ")
duration = float(input("Enter Duration (in mins): "))
genres = input("Enter Genres (comma-separated): ").split(",")
play_stats = (int(input("Enter Times Played: ")), int(input("Enter Likes: ")))
popularity_percent = float(input("Enter Popularity Percentage: "))
features = set(input("Enter Track Features (comma-separated): ").split(","))
artist_info = {
    "name": input("Enter Artist Name: "),
    "contact": input("Enter Artist Contact: "),
    "location": input("Enter Artist Location: ")
}

# Clean whitespace in list and set
genres = [genre.strip() for genre in genres]
features = {feature.strip() for feature in features}

# Task 2: Display Track Details using Different Formatting

print("\n🎧 --- TRACK INFO CARD --- 🎧\n")

# 1. Comma Separation
print("Track ID, Name, Duration:", track_id, track_name, duration, sep=', ')

# 2. Percentage Formatting (% operator)
print("Popularity: %.2f%%" % popularity_percent)

# 3. f-string Formatting
print(f"Track Name: {track_name}")
print(f"Duration: {duration} mins")
print(f"Times Played: {play_stats[0]} | Likes: {play_stats[1]}")
print(f"Genres: {', '.join(genres)}")
print(f"Features: {', '.join(features)}")

# 4. .format() method
print("Artist Info: Name - {}, Contact - {}, Location - {}".format(
    artist_info["name"], artist_info["contact"], artist_info["location"]))
