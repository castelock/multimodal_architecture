from Gesture_Recognition import GestureRecognition
from Speech_Recognition import SpeechRecognition
from interaction_manager import InteractionManager
from threading import Thread

def actGesture():
    interact_manager = InteractionManager()
    interact_manager.activateGestureInteraction()

def actUI():
    interact_manager = InteractionManager()
    interact_manager.activateUI()


"""t1 = Thread(target=actUI, daemon=True)
t2 = Thread(target=actGesture, daemon=True)

t1.start()
t2.start()"""

#t2.join()

app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()

gr = GestureRecognition()

sr = SpeechRecognition()

interaction_manager = InteractionManager(gr, sr, window)
interaction_manager.main_flow()

