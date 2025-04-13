import datetime
import os
import threading
import pyautogui
import webbrowser
import time
import pyttsx3
import pygame
import wave
import pyaudio
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import logging

# Set up logging
logging.basicConfig(
    filename='jarvis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize text-to-speech engine
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
except Exception as e:
    logging.error(f"Failed to initialize text-to-speech engine: {e}")
    raise

# Initialize pygame mixer for music playback
try:
    pygame.mixer.init()
except Exception as e:
    logging.error(f"Failed to initialize pygame mixer: {e}")
    raise

class JarvisInterface:
    def __init__(self):
        try:
            self.root = tk.Tk()
            self.root.title("Jarvis Assistant")
            self.root.geometry("800x600")
            self.root.configure(bg='#1e1e1e')
            
            self.conversation_history = []
            
            self.main_frame = tk.Frame(self.root, bg='#1e1e1e')
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            self.conversation_display = scrolledtext.ScrolledText(
                self.main_frame,
                wrap=tk.WORD,
                width=70,
                height=25,
                bg='#2d2d2d',
                fg='#ffffff',
                font=('Arial', 10)
            )
            self.conversation_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            self.conversation_display.config(state=tk.DISABLED)
            
            self.input_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
            self.input_frame.pack(fill=tk.X, padx=5, pady=5)
            
            self.input_field = tk.Entry(
                self.input_frame,
                width=60,
                bg='#2d2d2d',
                fg='#ffffff',
                font=('Arial', 10)
            )
            self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            self.input_field.bind('<Return>', self.send_message)
            
            self.send_button = tk.Button(
                self.input_frame,
                text="Send",
                command=self.send_message,
                bg='#007acc',
                fg='#ffffff',
                font=('Arial', 10)
            )
            self.send_button.pack(side=tk.RIGHT, padx=5)
            
            self.is_listening = False
            logging.info("Jarvis interface initialized successfully")
        except Exception as e:
            logging.error(f"Failed to initialize Jarvis interface: {e}")
            raise

    def add_message(self, sender, message):
        try:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            formatted_message = f"[{timestamp}] {sender}: {message}\n"
            
            self.conversation_history.append((sender, message, timestamp))
            
            self.conversation_display.config(state=tk.NORMAL)
            self.conversation_display.insert(tk.END, formatted_message)
            self.conversation_display.see(tk.END)
            self.conversation_display.config(state=tk.DISABLED)
            logging.info(f"Message added: {sender} - {message}")
        except Exception as e:
            logging.error(f"Failed to add message: {e}")
            raise
    
    def send_message(self, event=None):
        try:
            message = self.input_field.get().strip()
            if message:
                self.add_message("You", message)
                self.input_field.delete(0, tk.END)
                return message
            return None
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            raise
    
    def get_conversation_history(self):
        return self.conversation_history
    
    def start(self):
        try:
            self.root.mainloop()
        except Exception as e:
            logging.error(f"Failed to start interface: {e}")
            raise

class Jarvis:
    def __init__(self):
        self.interface = None
        self.is_listening = False
        self.safe_apps = {
            'chrome': 'chrome.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe'
        }
        logging.info("Jarvis initialized")
        
    def setup_interface(self):
        try:
            self.interface = JarvisInterface()
            logging.info("Interface setup completed")
        except Exception as e:
            logging.error(f"Failed to setup interface: {e}")
            raise
        
    def speak(self, text):
        try:
            if not isinstance(text, str):
                raise ValueError("Text must be a string")
            
            print(f"Speaking: {text}")
            if self.interface:
                self.interface.add_message("Jarvis", text)
            
            engine.say(text)
            engine.runAndWait()
            logging.info(f"Spoke text: {text}")
        except Exception as e:
            logging.error(f"Error speaking audio: {e}")
            if self.interface:
                self.interface.add_message("Jarvis", "I encountered an error while speaking")

    def take_command(self):
        try:
            if self.interface:
                message = self.interface.input_field.get().strip()
                if message:
                    self.interface.input_field.delete(0, tk.END)
                    self.interface.add_message("You", message)
                    return message.lower()
            return "none wake up"
        except Exception as e:
            logging.error(f"Error taking command: {e}")
            return "none wake up"

    def process_command(self, query):
        try:
            if not isinstance(query, str):
                raise ValueError("Query must be a string")
            
            query = query.strip().lower()
            
            if 'wake up' in query:
                self.speak("I'm awake and ready to help you, sir!")
                return True
            elif 'exit from here' in query or 'top' in query or 'go to sleep' in query:
                self.speak("Ok sir, You can call me anytime")
                return False
            elif "hello" in query:
                self.speak("Hello sir, How are you?")
            elif "i am fine" in query:
                self.speak("That's great sir")
            elif "how are you" in query or "how r u" in query:
                self.speak("Perfect Sir")
            elif "thank you" in query or "thanks" in query:
                self.speak("You are welcome, Sir")
            elif "google" in query:
                search_query = query.replace("google", "").strip()
                if search_query:
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif "youtube" in query:
                search_query = query.replace("youtube", "").strip()
                if search_query:
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            elif "wikipedia" in query:
                search_query = query.replace("wikipedia", "").strip()
                if search_query:
                    webbrowser.open(f"https://en.wikipedia.org/wiki/{search_query}")
            elif "temperature" in query or "weather" in query:
                try:
                    url = "https://www.google.com/search?q=temperature+in+my+location"
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                    r = requests.get(url, headers=headers, timeout=10)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    self.speak(f"Current temperature is {temp}")
                except Exception as e:
                    logging.error(f"Error fetching temperature: {e}")
                    self.speak("Sorry, I couldn't fetch the temperature at the moment.")
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak(f"Sir, the time is {strTime}")
            elif "set alarm" in query:
                try:
                    print("Input time example: 10 and 10 and 10")
                    self.speak("Set the time")
                    a = input("Please tell the time: ")
                    if re.match(r'^\d+ and \d+ and \d+$', a):
                        self.alarm(a)
                        self.speak("Done, sir")
                    else:
                        self.speak("Invalid time format. Please use the format: number and number and number")
                except Exception as e:
                    logging.error(f"Error setting alarm: {e}")
                    self.speak("Sorry, I couldn't set the alarm")
            elif "open" in query:
                app_name = query.replace("open", "").strip().lower()
                if app_name in self.safe_apps:
                    try:
                        os.startfile(self.safe_apps[app_name])
                    except Exception as e:
                        logging.error(f"Error opening application: {e}")
                        self.speak(f"Sorry, I couldn't open {app_name}")
                else:
                    self.speak("I don't know how to open that application")
            elif "close app" in query:
                app_name = query.replace("close app", "").strip().lower()
                if app_name in self.safe_apps:
                    try:
                        os.system(f"taskkill /f /im {self.safe_apps[app_name]}")
                    except Exception as e:
                        logging.error(f"Error closing application: {e}")
                        self.speak(f"Sorry, I couldn't close {app_name}")
                else:
                    self.speak("I don't know how to close that application")
            elif "play music" in query:
                try:
                    if os.path.exists("ksh.mp3"):
                        pygame.mixer.music.load("ksh.mp3")
                        pygame.mixer.music.play()
                    else:
                        self.speak("Music file not found")
                except Exception as e:
                    logging.error(f"Error playing music: {e}")
                    self.speak("Sorry, I couldn't play the music")
            else:
                self.speak("I didn't understand that")
            return True
        except Exception as e:
            logging.error(f"Error processing command: {e}")
            self.speak("I encountered an error while processing your command")
            return True

    def alarm(self, query):
        try:
            if not isinstance(query, str):
                raise ValueError("Query must be a string")
            
            with open("alarm.txt", "a") as timehere:
                timehere.write(query + "\n")
            os.startfile("alarm.py")
            logging.info(f"Alarm set for: {query}")
        except Exception as e:
            logging.error(f"Error setting alarm: {e}")
            self.speak("Sorry, I couldn't set the alarm")

    def start(self):
        try:
            def run_interface():
                self.setup_interface()
                self.interface.start()

            def run_jarvis():
                time.sleep(1)  # Wait for interface to initialize
                while True:
                    query = self.take_command()
                    if not self.process_command(query):
                        break

            # Start interface in the main thread
            interface_thread = threading.Thread(target=run_interface)
            interface_thread.start()

            # Start Jarvis in a separate thread
            jarvis_thread = threading.Thread(target=run_jarvis)
            jarvis_thread.daemon = True
            jarvis_thread.start()

            # Wait for interface thread to complete
            interface_thread.join()
            logging.info("Jarvis started successfully")
        except Exception as e:
            logging.error(f"Error starting Jarvis: {e}")
            raise

if __name__ == '__main__':
    try:
        jarvis = Jarvis()
        jarvis.start()
    except Exception as e:
        logging.error(f"Error starting Jarvis: {e}")
        messagebox.showerror("Error", "An error occurred while starting Jarvis. Please check the logs.")
    finally:
        try:
            pygame.mixer.quit()
        except:
            pass
