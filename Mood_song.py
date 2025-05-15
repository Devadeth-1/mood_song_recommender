from textblob import TextBlob
import random

# Step 1: Get user input
mood = input("How are you feeling today? ")
blob = TextBlob(mood)

# Step 2: Analyze sentiment polarity (-1 to 1)
sentiment = blob.sentiment.polarity

# Step 3: Define song lists for each mood category
very_happy_songs = [
    "'Happy' by Pharrell Williams",
    "'Uptown Funk' by Bruno Mars",
    "Pwoli Mood 🎉 - Munthirippadam (Malayalam)"
]

happy_songs = [
    "'Can't Stop the Feeling' by Justin Timberlake",
    "'Good Life' by OneRepublic",
    "Nesa Mood 🔥 - Vennilavu Nee (Malayalam)"
]

neutral_songs = [
    "'Let It Be' by The Beatles",
    "'Count on Me' by Bruno Mars",
    "'Imagine' by John Lennon"
]

sad_songs = [
    "'Fix You' by Coldplay",
    "'Someone Like You' by Adele",
    "Shokam Mood 💔 - Kuyilinte Paattu (Malayalam)"
]

very_sad_songs = [
    "'Let Her Go' by Passenger",
    "'Tears in Heaven' by Eric Clapton",
    "Shokam Mood 💔 - Kuyil Paatu Moham (Malayalam)"
]

# Step 4: Select song based on sentiment range
if sentiment >= 0.6:
    song = random.choice(very_happy_songs)
    print(f"🎵 You're very happy! Playing: {song}")
elif 0.3 <= sentiment < 0.6:
    song = random.choice(happy_songs)
    print(f"🎵 You're happy! Playing: {song}")
elif -0.3 <= sentiment < 0.3:
    song = random.choice(neutral_songs)
    print(f"🎵 You're neutral or unsure. Playing: {song}")
elif -0.6 <= sentiment < -0.3:
    song = random.choice(sad_songs)
    print(f"🎵 You're feeling low. Playing: {song}")
else:
    song = random.choice(very_sad_songs)
    print(f"🎵 You're very sad. Playing: {song}")
