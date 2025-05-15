import speech_recognition as sr
import pyttsx3
import time
import re
from textblob import TextBlob

# Initialize TTS engine
engine = pyttsx3.init()

# --- Set female voice ---
voices = engine.getProperty('voices')
female = next((v for v in voices if "female" in v.name.lower()), voices[0])
engine.setProperty('voice', female.id)

# --- Set slower rate ---
engine.setProperty('rate', 120)

# Helper to speak in chunks
def speak_text(text):
    chunks = re.split(r'(?<=[\.\!\?])\s+', text)
    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.9)

# Helper to speak a simple phrase
def speak(phrase):
    engine.say(phrase)
    engine.runAndWait()

# Listen and respond
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    speak("How are you feeling today?")
    audio = recognizer.listen(source)

try:
    mood_text = recognizer.recognize_google(audio)
    blob = TextBlob(mood_text)
    sentiment = blob.sentiment.polarity

    # Choose a song based on sentiment
    if sentiment > 0.3:
        song = "This Song Makes you Happy In PWOLI MOOOOD,                                                                  Xingunamani xingunamani Sritchuputta nenjul ani                           Hay venkal kinne venkal kinne Pola minnum mandra mani                            Naan wedkatouku bakshatil bhokadhav Oru noolilla     chel katta aalanav Nee vanta en panda kali  Ammangooooooooooooooooooooooooooooooooooooo        Ammangoooooooooooooooooooooo                Ammangoooooooooooo"
    elif sentiment < -0.3:
        song = "This Song Makes you Sad In SHOKAM MOOOOD                       Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee Neele Thaazhe Thaliraarnnu Poovanangal Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee"
    else:
        song = "This Song is NESA MOOOOD                        Koka koka koka kadithe Kora kora mantu choostharuPotti potti gowne vesthe Patti patti choostharu Koka kaadhu gownu Kaadhu kattulona yemundi Mee kallallone antha undhi Mee maga buddhe vankara buddhi     Oo antava mava OOo oo antava mava  OOOOo antava mava OOOo oo antava mava"

    # Announce recommendation
    speak(f"Based on your mood, I suggest: {song}")

    # If you want to read lyrics, do chunked reading:
    # lyrics = "..."  # load your lyrics here
    # speak_text(lyrics)

except Exception:
    speak("Sorry, I couldn't understand you. Please try again.")
