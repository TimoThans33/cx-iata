from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from tabs import MyTabWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window
        self.setWindowTitle('IATA analysis')
        self.setGeometry(50, 50, 1000, 1000)

        # tab widgets
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(Self.tab_widget)

        self.show()