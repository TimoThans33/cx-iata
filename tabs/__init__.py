from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize the tab screens
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(600, 400)

        # adding tabs
        self.tabs.addTab(self.tab1, "Activity")
        self.tabs.addTab(self.tab2, "Overview")
        self.tabs.addTab(self.tab3, "Advanced")
