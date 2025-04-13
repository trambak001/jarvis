import tkinter as tk
from tkinter import scrolledtext
import datetime

class JarvisInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jarvis Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#1e1e1e')
        
        # Conversation history
        self.conversation_history = []
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg='#1e1e1e')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create conversation display
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
        
        # Create input frame
        self.input_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create input field
        self.input_field = tk.Entry(
            self.input_frame,
            width=60,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Arial', 10)
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.input_field.bind('<Return>', self.send_message)
        
        # Create send button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            command=self.send_message,
            bg='#007acc',
            fg='#ffffff',
            font=('Arial', 10)
        )
        self.send_button.pack(side=tk.RIGHT, padx=5)
        
    def add_message(self, sender, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {sender}: {message}\n"
        
        self.conversation_history.append((sender, message, timestamp))
        
        self.conversation_display.config(state=tk.NORMAL)
        self.conversation_display.insert(tk.END, formatted_message)
        self.conversation_display.see(tk.END)
        self.conversation_display.config(state=tk.DISABLED)
    
    def send_message(self, event=None):
        message = self.input_field.get()
        if message:
            self.add_message("You", message)
            self.input_field.delete(0, tk.END)
            return message
        return None
    
    def get_conversation_history(self):
        return self.conversation_history
    
    def start(self):
        self.root.mainloop() 