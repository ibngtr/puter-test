import streamlit as st

import tkinter as tk
from tkinter import scrolledtext
import requests

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, f"You: {user_input}\n")
    chatbox.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
    response = requests.get(f"https://js.puter.com/v2/chat?text={user_input}").json()
    bot_response = response.get("response", "Sorry, I didn't understand that.")
    
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, f"Bot: {bot_response}\n")
    chatbox.config(state=tk.DISABLED)
    chatbox.yview(tk.END)

root = tk.Tk()
root.title("Chatbot")

chatbox = scrolledtext.ScrolledText(root, width=50, height=20, state=tk.DISABLED)
chatbox.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()

