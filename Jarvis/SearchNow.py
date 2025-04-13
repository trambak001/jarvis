import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def takeCommand():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        energy_thrashold = 400

        audio = r.listen(source, 0, 4)
    try:

        print("Understanding...")

        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")

    except Exception as e:

        print("speak That again")

        return "None"

    return query


query = takeCommand().lower()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchGoogle(query):
    if 'google' in query or 'Google search' in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)

    except:
        speak("No Speakable output available")


def searchYoutube(query):
    if 'youtube' in query:
        speak("This is What I found from youtube!")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("According to Wikipedia")
        query = query.replace("wikipedia", "")
        query = query.replace("Search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
