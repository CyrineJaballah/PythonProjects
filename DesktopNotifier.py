from win10toast import ToastNotifier
import time

def desktop_notifier(title, message):
    # Create a ToastNotifier object
    notifier = ToastNotifier()

    # Show the notification
    notifier.show_toast(title, message, duration=5)

# Example usage
title = "Desktop Notifier"
message = "This is a notification from the desktop notifier app."

# Send notifications every 5 seconds for a total of 5 times
for i in range(5):
    desktop_notifier(title, message)
    time.sleep(5)
