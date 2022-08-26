from Gesture_Recognition import GestureRecognition


import mediapipe as mp
import tensorflow as tf
# from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

class InteractionManager:
    interaction_event = None

    def __init__(self) -> None:
        pass

    def activateInteraction(self):
        
        gr = GestureRecognition()
        # gr.init_tensorflow()
        gr.recognize_handGestures()

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()



