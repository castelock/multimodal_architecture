import sys
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import speech_recognition as sr
import keyboard
from tensorflow.keras.models import load_model
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QFont
from threading import Thread


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Window width and height
        self.windowWidth = 800
        self.windowHeight = 600
           
        # setting the window size
        self.setGeometry(100, 60, self.windowWidth, self.windowHeight)

        self.setStyleSheet('background-color: rgb(49,96,148);')

        self.labelTitle = QLabel("FORMULARIO",self)

        self.labelTitle.move(int(0.35*self.windowWidth), int(0.1*self.windowHeight))

        self.labelTitle.setStyleSheet('font-weight: bold; color:white;')

        self.labelTitle.setFont(QFont('Arial', 30))

        self.labelTitle.adjustSize()

        self.labelName = QLabel("Nombre",self)

        self.labelName.move(int(0.33*self.windowWidth), int(0.3*self.windowHeight))

        self.labelName.setStyleSheet('font-weight: bold; color:white;')

        self.labelName.setFont(QFont('Arial', 14))

        self.textboxName = QLineEdit(self)

        self.textboxName.move(int(0.48*self.windowWidth), int(0.3*self.windowHeight))

        self.textboxName.setFixedWidth(200)

        self.textboxName.setStyleSheet('background-color:white;')

        self.labelLastName = QLabel("Apellidos",self)

        self.labelLastName.move(int(0.33*self.windowWidth), int(0.45*self.windowHeight))

        self.labelLastName.setStyleSheet('font-weight: bold; color:white;')

        self.labelLastName.setFont(QFont('Arial', 14))

        self.textboxLastName = QLineEdit(self)

        self.textboxLastName.move(int(0.48*self.windowWidth), int(0.45*self.windowHeight))
        
        self.textboxLastName.setFixedWidth(200)

        self.textboxLastName.setStyleSheet('background-color:white;')

        self.labelAge = QLabel("Edad",self)

        self.labelAge.move(int(0.33*self.windowWidth), int(0.6*self.windowHeight))        
        
        self.labelAge.setStyleSheet('font-weight: bold; color:white;')
        
        self.labelAge.setFont(QFont('Arial', 14))

        self.textboxAge = QLineEdit(self)

        self.textboxAge.move(int(0.48*self.windowWidth), int(0.6*self.windowHeight))

        self.textboxAge.setFixedWidth(200)

        self.textboxAge.setStyleSheet('background-color:white;')

        self.buttonSend = QPushButton("Enviar", self)

        self.buttonSend.move(int(0.35*self.windowWidth), int(0.8*self.windowHeight))

        self.buttonSend.setStyleSheet('border: 2px solid black; border-radius: 10px; background-color: rgb(0,141,191); font-weight: bold; color:white;')

        self.buttonSend.clicked.connect(self.createPopUpWindow)

        self.buttonExit = QPushButton("Salir", self)

        self.buttonExit.move(int(0.55*self.windowWidth), int(0.8*self.windowHeight))

        self.buttonExit.setStyleSheet('border: 2px solid black; border-radius: 10px; background-color: rgb(0,141,191); font-weight: bold; color:white;')

        self.buttonExit.clicked.connect(self.quitApp)

        # Label cam
        self.labelCam = QLabel()
        self.labelCam.move(int(0.1*self.windowWidth), int(0.6*self.windowHeight))
        self.labelCam.setFixedSize(240, 240)

        # Gesture recognition variables        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils
        self.model = load_model('mp_hand_gesture')
        self.className = "unkown" 
        self.popupWindowActivated = False

        # Speech recognition variables
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        self.speechCommand = "unkown" 

        


    def activateFocus(self, name):
        if(name=="textboxAge"):
            self.textboxAge.setFocus(True)
        else:
            print("The element has not been found")

    def recognizeGestures(self):
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
            img = QImage(framergb, framergb.shape[1], framergb.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            # self.labelCam.setPixmap(pix)
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

            # Show the final output
            #cv2.imshow("Output", frame)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.labelCam.setPixmap(pix)
            if gesture_rec == True:
                gesture_rec = False
                break

            # Send event if the gesture is well recognised
            if(self.className=="ok" or self.className=="fist" or self.className=="peace" or self.className=="thumbs up" or self.className=="thumbs down"):
                print("Gesture recognized!!")
                print("The gesture recognized is", self.className)
                self.commandUI()
                self.className = "unkown"
                # gesture_rec = True


           
        # release the webcam and destroy all active windows
        cap.release()

    def recognizeSpeech(self):
        while True:
            with self.mic as source:
                self.rec.adjust_for_ambient_noise(source)
                audio = self.rec.listen(source)
            
            try:
                self.speechCommand = self.rec.recognize_google(audio, language="es-ES")
            except sr.RequestError:
                # API was unreachable or unresponsive
                print("API unavailable")
            except sr.UnknownValueError:
                # speech was unintelligible
                print("Unable to recognize speech")
                    
            if(self.speechCommand == "nombre" or self.speechCommand == "apellidos" or self.speechCommand == "edad" or self.speechCommand == "enviar" or self.speechCommand == "salir"):
                self.commandUI()

            print(self.speechCommand)

    def commandUI(self):
        if(self.className=="fist" or self.speechCommand=="nombre"):
            self.textboxName.setFocus(True)
        elif(self.className=="peace" or self.speechCommand=="apellidos"):
            self.textboxLastName.setFocus(True)
        elif(self.className=="ok" or self.speechCommand=="edad"):
            self.textboxAge.setFocus(True)
        elif((self.className=="thumbs up" or self.speechCommand=="enviar") and self.popupWindowActivated == False):
            self.createPopUpWindow()
        elif(self.className=="thumbs down" or self.speechCommand=="salir"):
            QApplication.quit()
        else:
            print("Orden no identificado.")
    
    def setFocus(self, name):
        if(name=="textboxName"):
            self.textboxName.setFocus(True)
        elif(name=="textboxLastName"):
            self.textboxLastName.setFocus(True)
        elif(name=="textboxAge"):
            self.textboxAge.setFocus(True)
        else:
            print("Elemento de la interfaz de usuario no identificado.")

    def createPopUpWindow(self):
        self.popupWindowActivated = True
        msg = QMessageBox()
        msg.setWindowTitle("Formulario Enviado")
        msg.setText("Los datos del formulario fueron enviados.")
        result = msg.exec_()

        if(result == QMessageBox.Close):
            self.popupWindowActivated = False



    def quitApp(self):
        QApplication.quit()


# Starting the main flow of the GUI
app = QApplication(sys.argv)
window = MainWindow()

window.show()

# Gesture recognition thread
thread = Thread(target=window.recognizeGestures, daemon=True)
thread.start()

# Speech recognition thread
thread_speech = Thread(target=window.recognizeSpeech, daemon=True)
thread_speech.start()

app.exec()
