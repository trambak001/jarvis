import pyttsx3 as tts
import pyaudio
import speech_recognition

engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
engine.setProperty("rate", 200)

def say(text):
    try:
        print(f"speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"speak again: {e}")

def takeCommand():
    try:
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as sr:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(sr, 0, 3)
        print("repeating...")
        ans = r.recognize_google(audio, language='en-in')
        print(f"you said: {ans}")
        return ans
    except Exception as e:
        print(f"Error: {e}")
        return "none"

if __name__ == "__main__":
    while True:
        command = takeCommand().lower()
        say(command)