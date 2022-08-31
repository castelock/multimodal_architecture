from pydoc import classname
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from modality_component import ModalityComponent
from tensorflow.keras.models import load_model
from Event_handler import Event_Interaction

class GestureRecognition(ModalityComponent):


    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        self.model = load_model('mp_hand_gesture')
        self.gesture_event = Event_Interaction() 
        self.className = "unkown"      

  
    def init_tensorflow(self):
        # initialize mediapipe
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mpDraw = mp.solutions.drawing_utils

        # Load the gesture recognizer model
        model = load_model('mp_hand_gesture')
        # Load class names
        f = open('gesture.names', 'r')
        classNames = f.read().split('\n')
        f.close()
        print(classNames)
    
    # Methods to trigger a gesture event
    def raise_event(self):
        self.gesture_event()

    def AddSubscribersForGestureEvent(self,objMethod):
        self.gesture_event += objMethod
         
    def RemoveSubscribersForGestureEvent(self,objMethod):
        self.gesture_event -= objMethod

    # Main method to recognise a gesture
    def recognize_handGestures(self):
        # Variable to stop the loop when a gesture is recognised
        gesture_rec = False
        # Initialize the webcam for Hand Gesture Recognition Python project
        cap = cv2.VideoCapture(0)
        while True:
        # Read each frame from the webcam
            _, frame = cap.read()
            x , y, c = frame.shape
        # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get hand landmark prediction
            result = self.hands.process(framergb)
            # className = ''
            # Post process the result
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)
                        landmarks.append([lmx, lmy])
                    # Drawing landmarks on frames
                    self.mpDraw.draw_landmarks(frame, handslms, self.mpHands.HAND_CONNECTIONS)                    
                    # Load class names
                    f = open('gesture.names', 'r')
                    classNames = f.read().split('\n')
                    f.close()
                    # Predict gesture
                    prediction = self.model.predict([landmarks])
                    print(prediction)
                    classID = np.argmax(prediction)
                    self.className = classNames[classID]
            # Show the prediction on the frame
            cv2.putText(frame, self.className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

            # Send event if the gesture is well recognised
            if(self.className=="ok" or self.className=="fist" or self.className=="peace" or self.className=="thumbs up" or self.className=="thumbs down"):
                self.AddSubscribersForGestureEvent(self.send_event)
                self.raise_event()
                gesture_rec = True


            # Show the final output
            cv2.imshow("Output", frame)
            if cv2.waitKey(1) == ord('q') or gesture_rec == True:
                gesture_rec = False
                break
        # release the webcam and destroy all active windows
        cap.release()
        cv2.destroyAllWindows()

        return self.className


    def send_event(self):
        pass


   

