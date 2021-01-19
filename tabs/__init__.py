from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from glob import glob
import numpy as np

from tab1 import *
from tab2 import *
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize the tab screens
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab1_lib = tab1()

        self.tab2 = QWidget()
        self.tab2_lib = tab2()

        self.tab3 = QWidget()
        self.tabs.resize(600, 400)

        # adding tabs
        self.tabs.addTab(self.tab1, "Activity")
        self.tabs.addTab(self.tab2, "Overview")
        self.tabs.addTab(self.tab3, "Advanced")

        # create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.tab1_lib.btn)
        self.tab1_lib.btn.clicked.connect(self.getDirectories)

        self.tab1.layout.addWidget(self.tab1_lib.progress)
        self.tab1.layout.addWidget(self.tab1_lib.graphWidget)
        self.tab1.setLayout(self.tab1.layout)

        # create second tab
        self.tab2.layout = QVBoxLayout(self)

        #pie chart
        self.tab2.layout.addWidget(self.tab2_lib.chartview)
        
        self.tab2.sublayout_up = QHBoxLayout(self)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn1)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn2)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn15)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn3)
        
        self.tab2.sublayout_down = QHBoxLayout(self)
        #ocr
        self.ocrToLayout()
        #vcs
        self.vcsToLayout()
        #edi
        self.ediToLayout()
        #mes
        self.mesToLayout()

        self.tab2.layout.addLayout( self.tab2.sublayout_up )
        self.tab2.layout.addLayout( self.tab2.sublayout_down )

        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def getDirectories(self, s):
        self.completed = 0

        self.PATH = QFileDialog.getExistingDirectory(self,"Choose Directory", "C\\")

        print(self.PATH)
        self.EXT = '*.csv'
        self.all_csv_files = [file for path, subdir, files in os.walk(self.PATH) for file in glob(os.path.join(path, self.EXT))]

        self.li = []

        for filename in self.all_csv_files:
            self.df = pd.read_csv(filename, sep=";", index_col=None, header=0)
            self.li.append(self.df)
            self.completed += 100 / len(self.all_csv_files)
            self.tab1_graph.progress.setValue(self.completed)
        self.tab1_graph.progress.setValue(100)
        self.frame = pd.concat(self.li, axis=0, ignore_index=True)
        # read usefull data
        self.data = self.frame[["LicensePlate","Barcode", "Tunnel", "Source", "DestinationAirport", "ItemTime (local date)","Status", "PieceId"]]
        # show dates in plot
        self.dates = self.data.groupby(["ItemTime (local date)"])["PieceId"].count()
        self.keys = self.dates.keys()
        self.plot(np.linspace(0, 10, len(self.dates)), self.dates, "activity", 'r')

        # process data
        self.data_count = self.data.groupby(["Source"]).count()
        self.status_count = self.data.groupby(["Source","Status"])["PieceId"].count()
    
    def ocrToLayout(self):
        self.tab2.ocrlayout = QVBoxLayout(self)

        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn4)
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn5)
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn6)
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn7)
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn8)

        self.tab2.sublayout_down.addLayout( self.tab2.ocrlayout )

        self.tab2.ocrcomb = QVBoxLayout(self)

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox1)
        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox2)
        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox3)
        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox4)
        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox5)

        self.tab2.sublayout_down.addLayout( self.tab2.ocrcomb )

    def vcsToLayout(self):
        self.tab2.vcslayout = QVBoxLayout(self)

        self.tab2.vcslayout.addWidget(self.tab2_lib.btn10)
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn11)
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn12)
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn13)

        self.tab2.sublayout_down.addLayout( self.tab2.vcslayout )

        self.tab2.vcscomb = QVBoxLayout(self)

        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox6 )
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox7 )
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox8 )
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox9 )

        self.tab2.sublayout_down.addLayout( self.tab2.vcscomb )

    def ediToLayout(self):
        self.tab2.edilayout = QVBoxLayout(self)

        self.tab2.edilayout.addWidget(self.tab2_lib.btn16)
        self.tab2.edilayout.addWidget(self.tab2_lib.btn17)
        self.tab2.edilayout.addWidget(self.tab2_lib.btn18)

        self.tab2.sublayout_down.addLayout( self.tab2.edilayout )

        self.tab2.edicomb = QVBoxLayout(self)

        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox11)
        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox12)
        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox13)

        self.tab2.sublayout_down.addLayout( self.tab2.edicomb )

    def mesToLayout(self):
        self.tab2.meslayout = QVBoxLayout(self)

        self.tab2.meslayout.addWidget(self.tab2_lib.btn14)

        self.tab2.sublayout_down.addLayout( self.tab2.meslayout )

        self.tab2.mescomb = QVBoxLayout(self)
        
        self.tab2.mescomb.addWidget( self.tab2_lib.comboBox10 )

        self.tab2.sublayout_down.addLayout( self.tab2.mescomb )
