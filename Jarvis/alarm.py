import datetime
import os

import pyttsx3 as tts

engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 160)


def speak(text):
    try:
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking audio: {e}")


def alarm(query):
    timehere = open("alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


extractedtime = open("alarm.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

datetime = open("alarm.txt", "r+")
datetime.truncate(0)
datetime.close()


def ring(time):
    """

    :type time: time
    """
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set alarm", "")
    alarmtime = str(timenow)
    print(alarmtime)

    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == alarmtime:
            speak("Wake Up! It's time to wake up!")
            os.startfile("mp3.mp3")
        elif currenttime + "00:00:30" == alarmtime:
            exit()


ring(time)
