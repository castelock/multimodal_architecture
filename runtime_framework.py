from Gesture_Recognition import GestureRecognition
from Speech_Recognition import SpeechRecognition
from interaction_manager import InteractionManager
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap
from MainWindow import MainWindow



app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()

gr = GestureRecognition()

sr = SpeechRecognition()

interaction_manager = InteractionManager(gr, sr, window)
interaction_manager.main_flow()

