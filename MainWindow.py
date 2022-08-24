import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Layout
        layout = QGridLayout()
        #layout.setSpacing(10)

        layout.addWidget(QLabel("Nombre"), 1, 1)
        layout.addWidget(QLineEdit(), 1, 2)
        layout.addWidget(QLabel("Apellidos"), 2, 1)
        layout.addWidget(QLineEdit(), 2, 2)
        layout.addWidget(QLabel("Edad"), 3, 1)
        layout.addWidget(QLineEdit(), 3, 2)
        layout.addWidget(QPushButton("Enviar"), 4, 3)
        
        self.setGeometry(100, 60, 1000, 800)

        # self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)        
        
        
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
# setting  the size of window
# setGeometry(left, top, width, height)
#window.setGeometry(100, 60, 1000, 800)

window.show()

app.exec()
