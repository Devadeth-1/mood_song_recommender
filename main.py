import speech_recognition as sr
import pyttsx3
from textblob import TextBlob

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

rec = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    audio = rec.listen(source)

try:
    mood = rec.recognize_google(audio)
    print("You said:", mood)
    blob = TextBlob(mood)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.3:
        song = "Happy by Pharrell Williams"
    elif sentiment < -0.3:
        song = "Fix You by Coldplay"
    else:
        song = "Let It Be by The Beatles"

    speak(f"Based on your mood, I suggest: {song}")
except Exception as e:
    speak("Sorry, I couldn't understand you.")
