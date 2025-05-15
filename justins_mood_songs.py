from textblob import TextBlob
from playsound import playsound
import random
import os

# === Step 1: Play the mood question audio ===
playsound('temp_audio/justin.mp3')

# === Step 2: Get user input ===
mood_input = input("Type your mood response: ")
blob = TextBlob(mood_input)
sentiment = blob.sentiment.polarity

# === Step 3: Create mood-based MP3 playlists ===
very_happy_songs = ['temp_audio/very_happy1.mp3']
happy_songs = ['temp_audio/happy1.mp3']
neutral_songs = ['temp_audio/neutral1.mp3']
sad_songs = ['temp_audio/sad1.mp3']
very_sad_songs = ['temp_audio/very_sad1.mp3']

# === Step 4: Match sentiment and play a random song ===
if sentiment >= 0.6:
    song = random.choice(very_happy_songs)
    print("🎵 You're very happy! Playing a joyful song...")
elif 0.3 <= sentiment < 0.6:
    song = random.choice(happy_songs)
    print("🎵 You're happy! Enjoy your mood with this song...")
elif -0.3 <= sentiment < 0.3:
    song = random.choice(neutral_songs)
    print("🎵 You seem neutral. Here's something calming...")
elif -0.6 <= sentiment < -0.3:
    song = random.choice(sad_songs)
    print("🎵 You're feeling a bit low. Here's a song for you...")
else:
    song = random.choice(very_sad_songs)
    print("🎵 You seem really down. Playing something comforting...")

# === Step 5: Play selected song ===
playsound(song)
