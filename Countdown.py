import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, minutes=0, seconds=0):
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = minutes * 60 + seconds
        self.is_running = False

        self.window = tk.Tk()
        self.window.title("Countdown Timer")

        self.label = tk.Label(self.window, text="", font=("Arial", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(
            self.window, text="Start", command=self.start_timer, font=("Arial", 16)
        )
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(
            self.window, text="Stop", command=self.stop_timer, font=("Arial", 16), state=tk.DISABLED
        )
        self.stop_button.pack(pady=10)

    def update_label(self):
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_string)

    def countdown(self):
        if self.total_seconds > 0 and self.is_running:
            self.total_seconds -= 1
            self.update_label()
            self.window.after(1000, self.countdown)
        elif self.total_seconds == 0 and self.is_running:
            self.is_running = False
            self.stop_timer()
            messagebox.showinfo("Time's up!", "The countdown timer has finished.")

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.countdown()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run(self):
        self.update_label()
        self.window.mainloop()

if __name__ == "__main__":
    timer = CountdownTimer(minutes=1, seconds=30)
    timer.run()
