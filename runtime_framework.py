from Gesture_Recognition import GestureRecognition
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

interaction_manager = InteractionManager()
interaction_manager.activateGestureInteraction()



"""interact_manager.activateUI()
interact_manager.activateGestureInteraction()"""