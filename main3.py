import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which
import os
import time

# Setup ffmpeg path for pydub
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Create a temporary audio folder if not exists
TEMP_AUDIO_DIR = os.path.join(os.getcwd(), 'temp_audio')
if not os.path.exists(TEMP_AUDIO_DIR):
    os.makedirs(TEMP_AUDIO_DIR)

# Speak function using gTTS in Malayalam
def speak(text, filename="output.mp3", lang='ml'):
    filepath = os.path.join(TEMP_AUDIO_DIR, filename)
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filepath)

    song = AudioSegment.from_mp3(filepath)
    play(song)

    os.remove(filepath)  # Clean up

# Main program
def main():
    recognizer = sr.Recognizer()
    language_code = 'ml'

    with sr.Microphone() as source:
        speak("ഹായ്! ഇന്നത്തെ നിങ്ങളുടെ മനോഭാവം എങ്ങനെയുണ്ട്?")
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech in Malayalam
        mood_text = recognizer.recognize_google(audio, language=language_code)
        print("You said:", mood_text)

        # Since TextBlob doesn't support Malayalam, assume neutral mood
        sentiment = 0.0

        # Choose a song based on mood (you can later replace with ML model if needed)
        song = """ഈ പാട്ട് നിങ്ങളുടെ മനോഭാവത്തിന് അനുയോജ്യം ആണ് 🔥

എന്റെ ഖൽബിലെ വെണ്ണിലാവു നീ നല്ല പാട്ടുകാരാ
തട്ടമിട്ടു ഞാൻ കാത്തുവച്ചൊരെൻ മുല്ലമൊട്ടിലൂറും
അത്തറൊന്നു വേണ്ടേ 
എന്റെ ഖൽബിലെ വെണ്ണിലാവു നീ നല്ല പാട്ടുകാരാ
തട്ടമിട്ടു ഞാൻ കാത്തുവച്ചൊരെൻ മുല്ലമൊട്ടിലൂറും
അത്തറൊന്നു വേണ്ടേ

അത്തറൊന്നു വേണ്ടേ എന്റെ കൂട്ടുകാരാ,
സുൽത്താന്റെ ചേലുകാരാ"""

        speak("നിന്റെ മനോഭാവം അനുസരിച്ച് ഈ പാട്ട് കേൾക്കൂ!")
        time.sleep(1)
        speak(song, filename="mood_song.mp3", lang='ml')

    except Exception as e:
        speak("ക്ഷമിക്കണം, ഞാൻ മനസ്സിലാക്കിയില്ല. ദയവായി വീണ്ടും ശ്രമിക്കൂ.")
        print("Error:", e)

if __name__ == "__main__":
    main()
