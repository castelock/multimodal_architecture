from Gesture_Recognition import GestureRecognition


import mediapipe as mp
import tensorflow as tf
from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

gr = GestureRecognition()
# gr.init_tensorflow()
# gr.recognize_handGestures()

sr = SpeechRecognition()
# sr.list_mics()
sr.speechRecognition()
