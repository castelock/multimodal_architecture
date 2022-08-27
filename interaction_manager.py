from Gesture_Recognition import GestureRecognition
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor

import sys
import mediapipe as mp
import tensorflow as tf
# from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

class InteractionManager:
    interaction_event = "unkown"

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def activateUI(self):                

        self.window.show()

        app.exec()

    def activateGestureInteraction(self):
        
        gr = GestureRecognition()
        
        className = gr.recognize_handGestures()

        print("The prediction is", className)

        self.window.activateFocus("textboxaAge")

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()
    
    



