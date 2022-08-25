import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # Window width and height
        self.windowWidth = 1000
        self.windowHeight = 800

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
        
        # setting  the size of window
        # setGeometry(left, top, width, height)
        self.setGeometry(100, 60, self.windowWidth, self.windowHeight)

        self.labelTitle = QLabel("FORMULARIO",self)

        self.labelTitle.move(int(0.5*self.windowWidth), int(0.1*self.windowHeight))

        # TO DO Use setStyleSheet to modify the widget's properties.

        self.labelName = QLabel("Nombre",self)

        self.labelName.move(int(0.1*self.windowWidth), int(0.2*self.windowHeight))

        self.textboxName = QLineEdit(self)

        self.textboxName.move(int(0.2*self.windowWidth), int(0.2*self.windowHeight))

        self.labelLastName = QLabel("Apellidos",self)

        self.labelLastName.move(int(0.1*self.windowWidth), int(0.3*self.windowHeight))

        self.labelAge = QLabel("Edad",self)

        self.labelAge.move(int(0.1*self.windowWidth), int(0.4*self.windowHeight))

        # self.setLayout(layout)
        """widget = QWidget()
        widget.setLayout(layout)        
        
        
        self.setCentralWidget(widget)"""



app = QApplication(sys.argv)

window = MainWindow()

#window.setGeometry(100, 60, 1000, 800)

window.show()

app.exec()
