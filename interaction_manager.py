from Gesture_Recognition import GestureRecognition


import mediapipe as mp
import tensorflow as tf
# from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

class InteractionManager:
    interaction_event = "unkown"

    def __init__(self) -> None:
        pass

    def activateInteraction(self):
        
        gr = GestureRecognition()
        # gr.init_tensorflow()
        gr.recognize_handGestures()

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()
    
    # TODO Provisional content
    def act_gesture_recognition(self):
        if(self.interaction_event=="ok"):
            print("The gesture recognised is ok")
        elif(self.interaction_event=="fist"):
            print("The gesture recognised is fist")
        elif(self.interaction_event=="peace"):
            print("The gesture recognised is peace")
        elif(self.interaction_event=="thumbs up"):
            print("The gesture recognised is thumb up")
        elif(self.interaction_event=="thumbs down"):
            print("The gesture recognised is thumb down")
        else:
            print("The gesture is unkown.")



