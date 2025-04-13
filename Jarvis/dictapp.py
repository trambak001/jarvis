import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandpromt":"cmd","paint":"paint",
                                "word":"winword",
                                "excel":"excel",
                                "chrome":"chrome",
                                "vscode":"code",
                                "Powerpoint":"powerpnt",
                                "calculater":"calc",
                                "camera":"start microsoft.windows.camera:",
                                "sql":"E:\oracle\product\10.2.0\db_1\BIN\sqlplusw.exe",
                                "sql cammandline":"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
                                }
    
def openappweb(query):
    speak("launching,Sir")
    if ".com" in query or ".co.in" in  query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system("start "+{dictapp[app]})
    
    speak("Here it is")

def closeappweb(query):
    speak("closing,Sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys)
        for app in keys:
            if app in query:
                os.system(f"taskkill /im {dictapp[app]}exe")
                speak(f"{app} closed")
    