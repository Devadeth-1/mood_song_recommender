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
        song = "Xingunamani xingunamani Sritchuputta nenjul ani                           Hay venkal kinne venkal kinne Pola minnum mandra mani                            Naan wedkatouku bakshatil bhokadhav Oru noolilla     chel katta aalanav Nee vanta en panda kali  Ammangooooooooooooooooooooooooooooooooooooo        Ammangoooooooooooooooooooooo                Ammangoooooooooooo"
    elif sentiment < -0.3:
        song = "Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee Neele Thaazhe Thaliraarnnu Poovanangal Moham Kondu Njaan Dhooreyetho Eenam Pootha Naal Madhu Thedi Poyee"
    else:
        song = "Koka koka koka kadithe Kora kora mantu choostharuPotti potti gowne vesthe Patti patti choostharu Koka kaadhu gownu Kaadhu kattulona yemundi Mee kallallone antha undhi Mee maga buddhe vankara buddhi     Oo antava mava OOo oo antava mava  OOOOo antava mava OOOo oo antava mava"

    speak(f"Based on your mood, I suggest: {song}")
except Exception as e:
    speak("Sorry, I couldn't understand you.")





