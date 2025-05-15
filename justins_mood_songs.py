import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr
from textblob import TextBlob
from playsound import playsound
import random
import os

# === Step 1: Play the mood question using justin.mp3 ===
playsound('temp_audio/justin.mp3')

# === Step 2: Record user voice for 5 seconds ===
fs = 44100  # Sample rate
seconds = 5

print("🎙️ Recording your response for 5 seconds...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float32')
sd.wait()

# Convert to PCM format (int16) and save
recording_int16 = np.int16(recording * 32767)
write("user_mood.wav", fs, recording_int16)

# === Step 3: Convert speech to text ===
recognizer = sr.Recognizer()
with sr.AudioFile("user_mood.wav") as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("🗣️ You said:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand your voice.")
        exit()
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")
        exit()

# === Step 4: Analyze sentiment using TextBlob ===
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f"🧠 Sentiment Score: {sentiment}")

# === Step 5: Define mood-based song lists ===
very_happy_songs = ['temp_audio/very_happy1.mp3']
happy_songs = ['temp_audio/happy1.mp3']
neutral_songs = ['temp_audio/neutral1.mp3']
sad_songs = ['temp_audio/sad1.mp3']
very_sad_songs = ['temp_audio/very_sad1.mp3']

# === Step 6: Match mood and play song ===
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

playsound(song)
