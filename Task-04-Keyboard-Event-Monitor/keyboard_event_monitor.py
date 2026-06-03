import tkinter as tk
from datetime import datetime

LOG_FILE = "keystrokes.txt"

def log_key(event):
    key = event.keysym

    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {key}\n")

    status_label.config(text=f"Last Key Pressed: {key}")

root = tk.Tk()
root.title("Keyboard Event Monitor")
root.geometry("500x300")

title = tk.Label(
    root,
    text="Keyboard Event Monitor",
    font=("Arial", 16)
)
title.pack(pady=10)

info = tk.Label(
    root,
    text="Click inside this window and press keys.\nAll key presses will be saved to keystrokes.txt",
    font=("Arial", 10)
)
info.pack(pady=10)

status_label = tk.Label(
    root,
    text="No key pressed yet",
    font=("Arial", 12)
)
status_label.pack(pady=20)

root.bind("<Key>", log_key)

root.mainloop()