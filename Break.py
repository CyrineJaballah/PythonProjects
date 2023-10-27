import time
import tkinter as tk
from tkinter import messagebox

# Function to display reminder message
def remind():
    messagebox.showinfo("Take a Break", "It's time to take a short break!")

# Function to start the reminder loop
def start_reminder():
    while True:
        remind()
        time.sleep(1800)  # Remind every 30 minutes (1800 seconds)

# Create the GUI window
window = tk.Tk()
window.title("Break Reminder")

# Start reminder button
start_button = tk.Button(window, text="Start Reminder", command=start_reminder)
start_button.pack(pady=20)

# Run the GUI event loop
window.mainloop()
