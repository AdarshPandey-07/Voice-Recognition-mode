import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox
import numpy as np
from scipy.io.wavfile import read
import tensorflow as tf
from tensorflow import keras
from tempfile import NamedTemporaryFile

# Function to load the trained model
def load_model():
    model = keras.models.load_model("model.keras")
    return model

# Function to recognize speaker
def recognize_speaker(audio_file):
    # Load the audio file
    sample_rate, audio_data = read(audio_file)
    
    # Preprocess audio data (you may need to adjust this based on your preprocessing)
    # For example, you may need to resample the audio data to 16000 Hz
    
    # Perform speaker recognition using the loaded model
    # (you need to implement this part based on your model)
    # Here's a placeholder implementation:
    speaker_id = np.random.randint(0, 5)  # Placeholder random speaker ID
    
    return speaker_id

class SpeakerRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speaker Recognition")
        
        # Load the model
        self.model = load_model()
        
        # Create GUI elements
        self.label = QLabel("Select an audio file (.wav) to recognize speaker:")
        self.button = QPushButton("Select File")
        self.button.clicked.connect(self.select_file)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def select_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Select WAV File", "", "WAV files (*.wav)")
        if filepath:
            speaker_id = recognize_speaker(filepath)
            QMessageBox.information(self, "Speaker Recognition", f"The predicted speaker ID is: {speaker_id}")

def main():
    app = QApplication(sys.argv)
    window = SpeakerRecognitionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
