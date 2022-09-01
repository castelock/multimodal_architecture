from Gesture_Recognition import GestureRecognition
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor

import sys
import mediapipe as mp
import tensorflow as tf
import asyncio
# from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

class InteractionManager:
    

    """def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def activateUI(self):                

        self.window.show()

        self.app.exec()

    def activateGestureInteraction(self):
        
        gr = GestureRecognition()
        
        className = gr.recognize_handGestures()

        print("The prediction is", className)

        self.window.activateFocus("textboxaAge")

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()"""

    phase = None
    def __init__(self, gestureRecognitionMC, gui):
        self.gestureRecognitionMC = gestureRecognitionMC
        self.gui = gui
        self.waitSignal = False  

             

        

    async def main_flow(self):
        
        self.gestureRecognitionMC.recognize_handGestures()

        while (InteractionManager.phase != "exit"):
            if(InteractionManager.phase=="gesture_recognised"):
                message = self.action_UI()
                self.gestureRecognitionMC.set_response(message)        
        

        
    def action_UI(self):
        gesture = self.gestureRecognitionMC.getGesture()
        message = " "
        if(gesture =="fist" or self.speechCommand=="nombre"):
            self.gui.setFocus("textboxName")
            message = "Acción realizada correctamente"
        elif(gesture=="peace" or self.speechCommand=="apellidos"):
            self.gui.setFocus("textboxLastName")
            message = "Acción realizada correctamente"
        elif(gesture=="ok" or self.speechCommand=="edad"):
            self.gui.setFocus("textboxAge")
            message = "Acción realizada correctamente"
        elif(gesture=="thumbs up" or self.speechCommand=="enviar"):
            self.gui.createPopUpWindow()
            message = "Acción realizada correctamente"
        elif(gesture=="thumbs down" or self.speechCommand=="salir"):
            self.gui.quitApp()
            message = "Acción realizada correctamente"
        else:
            print("Acción no identificada.")
            message = "Acción fallida"
        
        return message
    

    async def wait_response(self):
        while(self.waitSignal == False):
            print("Esperando la respuesta del GUI")
        
        self.waitSignal = False
        return self.responseIM

