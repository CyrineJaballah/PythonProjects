import tkinter as tk
import speedtest
from speedtest import SpeedtestException

def check_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1000000  # Convert to Mbps
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        result_label.config(
            text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps"
        )
    except SpeedtestException as e:
        result_label.config(text="Error occurred while testing the speed.")

# Create the GUI window
window = tk.Tk()
window.title("Internet Speed Checker")

# Check speed button
check_button = tk.Button(window, text="Check Speed", command=check_speed)
check_button.pack(pady=20)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 16), wraplength=400)
result_label.pack()

# Run the GUI event loop
window.mainloop()
