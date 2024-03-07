import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
from scipy.io.wavfile import read
import tensorflow as tf
from tensorflow import keras

# Function to load the trained model
def load_model():
    model = keras.models.load_model("model.keras")
    return model

# Function to recognize speaker
def recognize_speaker(audio_file):
    # Placeholder function to simulate speaker recognition
    speaker_id = np.random.randint(0, 5)  # Placeholder random speaker ID
    return speaker_id

# Function to handle file selection
def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if filepath:
        speaker_id = recognize_speaker(filepath)
        messagebox.showinfo("Speaker Recognition", f"The predicted speaker ID is: {speaker_id}")

# Function to create the GUI
def create_gui():
    # Create the root window
    root = tk.Tk()
    root.title("Speaker Recognition")
    
    # Set background image
    background_image = tk.PhotoImage(file=r"C:\Users\Adarsh\Downloads\images.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window dimensions and position
    window_width = 400
    window_height = 200
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Create GUI elements
    label = ttk.Label(root, text="Select an audio file (.wav) to recognize speaker:", foreground="white", background="#333")
    label.pack(pady=10)

    button = ttk.Button(root, text="Select File", command=select_file)
    button.pack(pady=5)

    # Start the main event loop
    root.mainloop()

create_gui()
