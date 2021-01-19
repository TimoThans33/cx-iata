import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *

import pandas as pd
import matplotlib.pyplot as plt 
import os
from glob import glob
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

# dummy data
data = {'col1':['1','2','3','4'],
        'col2':['1','2','3','4'],
        'col3':['1','2','3','4']}

# Creating the main window
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        # main window
        self.setWindowTitle('IATA analysis')
        self.setGeometry(50, 50, 1000, 1000)
        
        # tab widgets
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()

# Creating tab widgets
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(600,400)

        # Add tabs
        self.tabs.addTab(self.tab1, "Activity")
        self.tabs.addTab(self.tab2, "Overview")
        self.tabs.addTab(self.tab3, "Advanced")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1_interface()
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.sublayout_up = QHBoxLayout(self)
        self.tab2.sublayout_down = QHBoxLayout(self)
        self.tab2.ocrlayout = QVBoxLayout(self)
        self.tab2.ocrcomb = QVBoxLayout(self)
        self.tab2.vcslayout = QVBoxLayout(self)
        self.tab2.vcscomb = QVBoxLayout(self)
        self.tab2.meslayout = QVBoxLayout(self)
        self.tab2.mescomb = QVBoxLayout(self)
        self.tab2.edilayout = QVBoxLayout(self)
        self.tab2.edicomb = QVBoxLayout(self)
        
        self.tab2_interface()
        self.tab2.layout.addLayout( self.tab2.sublayout_up )
        self.tab2.layout.addLayout( self.tab2.sublayout_down )
        self.tab2.setLayout(self.tab2.layout)

        # Create third tab
        self.tab3.layout = QVBoxLayout(self)
        self.tab3_interface()
        self.tab3.setLayout(self.tab3.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def tab1_interface(self):
        self.btn = QPushButton("Folder", self)
        self.btn.clicked.connect(self.getDirectories)
        self.btn.adjustSize()
        self.tab1.layout.addWidget(self.btn)

        self.progress = QProgressBar(self)
        self.progress.adjustSize()
        self.tab1.layout.addWidget(self.progress)

        self.graphWidget = pg.PlotWidget()
        self.tab1.layout.addWidget(self.graphWidget)

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add title
        self.graphWidget.setTitle("Activity", color="r", size="10pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Bags", **styles)
        self.graphWidget.setLabel("bottom", "Time", **styles)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20000, 55000, padding=0)

    def tab2_interface(self):

        # values
        self.OCR_edi_ocr = 0
        self.OCR_edi_ocr = 0
        self.OCR_edi_ocr_vcs = 0
        self.OCR_ocr_edi = 0
        self.OCR_ocr_ocr = 0
        self.OCR_ocr_vcs = 0
        self.VCS_vcs = 0
        self.VCS_vcs_vcs = 0 
        self.VCS_vcs_edi = 0
        self.VCS_edi_vcs = 0
        self.MES_vcs_vcs = 0
        self.EDI_edi = 0
        self.EDI_edi_edi = 0
        self.EDI_edi_edi_edi = 0
        # series for piechart
        self.series = QPieSeries()
        # OCR

        self.ocr()

        # VCS

        self.vcs()
        
        # MES

        self.mes()

        # EDI

        self.edi()

        self.add_layout()

        # data

        self.update_piechart()

        # adding slices
        slice = QPieSlice()
        slice = self.series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.tab2.layout.addWidget(chartview)

        self.sl = QSlider(Qt.Horizontal, self)
        self.sl.valueChanged[int].connect(self.valuechange)

        self.tab2.layout.addWidget(self.sl)

    def tab3_interface(self):
        items = ["noEDI", "EDI"]
        self.comboBox_Y = QComboBox()

        self.comboBox_Y.addItems(items)
        
        self.comboBox_Y.adjustSize()
        self.tab3.layout.addWidget(self.comboBox_Y)
        self.comboBox_Y.activated[str].connect(self.selectionchange_occurences_Y)

        self.create_bar()

    def valuechange(self):
        size = self.sl.value()
        print("slide bar : ",size)

    def btnstate_ocr(self, b):
        if b.text() == "EDI+OCR":
            if b.isChecked() == True:
                self.OCR_edi_ocr = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "EDI+OCR+VCS":
            if b.isChecked() == True:
                self.OCR_edi_ocr_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "OCR+EDI":
            if b.isChecked() == True:
                self.OCR_ocr_edi = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "OCR+OCR":
            if b.isChecked() == True:
                self.OCR_ocr_ocr = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "OCR+VCS":
            if b.isChecked() == True:
                self.OCR_ocr_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
    def btnstate_vcs(self, b):
        if b.text() == "VCS":
            if b.isChecked() == True:
                self.VCS_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "VCS+VCS":
            if b.isChecked() == True:
                self.VCS_vcs_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "VCS+EDI":
            if b.isChecked() == True:
                self.VCS_vcs_edi = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "EDI+VCS":
            if b.isChecked() == True:
                self.VCS_edi_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
    def btnstate_mes(self, b):
        if b.text() == "MES_vcs_vcs":
            if b.isChecked() == True:
                self.MES_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
    def btnstate_vcs(self, b):
        if b.text() == "EDI":
            if b.isChecked() == True:
                self.VCS_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "EDI+EDI":
            if b.isChecked() == True:
                self.VCS_vcs_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
        if b.text() == "EDI+EDI+EDI":
            if b.isChecked() == True:
                self.VCS_vcs_edi = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")
    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

    def getDirectories(self, s):
        print("click", s)
        self.completed = 0

        self.PATH = QFileDialog.getExistingDirectory(self, "Choose Directory", "C:\\")

        print(self.PATH)

        self.EXT = '*.csv'
        self.all_csv_files = [file for path, subdir, files in os.walk(self.PATH) for file in glob(os.path.join(path, self.EXT))]    

        print(len(self.all_csv_files))

        self.li = []

        # self.contents.setText(str(len(all_csv_files)))

        for filename in self.all_csv_files:
            self.df = pd.read_csv(filename, sep=";", index_col=None, header=0)
            self.li.append(self.df)
            self.completed += 100 / len(self.all_csv_files)
            self.progress.setValue(self.completed)
        self.progress.setValue(100)
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

    def update_piechart(self):
        self.OCR = self.OCR_edi_ocr + self.OCR_edi_ocr_vcs + self.OCR_ocr_edi + self.OCR_ocr_ocr + self.OCR_ocr_vcs
        self.VCS = self.VCS_vcs + self.VCS_vcs_vcs + self.VCS_vcs_edi + self.VCS_edi_vcs
        self.MES = self.MES_vcs_vcs
        self.EDI = self.EDI_edi + self.EDI_edi_edi + self.EDI_edi_edi_edi

        self.series.clear()

        self.series.append("OCR", self.OCR)
        self.series.append("VCS", self.VCS)
        self.series.append("MES", self.MES)
        self.series.append("EDI", self.EDI)

        print("OCR",self.OCR,"VCS", self.VCS,"MES",self.MES,"EDI",self.EDI)

    def create_bar(self):
        # The QBarSet class represents a set of bars

        self.set0 = QBarSet("OCR")
        self.set1 = QBarSet("EDI")
        self.set2 = QBarSet("VCS")
        self.set3 = QBarSet("MES")
        self.set4 = QBarSet("VCS2")

        self.set0 << 1 << 2 << 3 << 4 << 5 << 6
        self.set1 << 5 << 0 << 0 << 4 << 0 << 7
        self.set2 << 3 << 5 << 8 << 13 << 8 << 5
        self.set3 << 5 << 6 << 7 << 3 << 4 << 5
        self.set4 << 9 << 7 << 5 << 3 << 1 << 2

        self.bar_series = QPercentBarSeries()
        self.bar_series = QPercentBarSeries()
        self.bar_series.append(self.set0)
        self.bar_series.append(self.set1)
        self.bar_series.append(self.set2)
        self.bar_series.append(self.set3)
        self.bar_series.append(self.set4)

        self.chart = QChart()
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle("Percent Example")
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.categories = ["000", "2S35", "523", "555", "016"]
        self.axis = QBarCategoryAxis()
        self.axis.append(self.categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axis, self.bar_series)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.tab3.layout.addWidget(self.chartView)

    def update_bar(self):

        self.set0 << self.data_Y["000"]
        self.set1 << self.data_Y["235"]
        self.set2 << self.data_Y["523"]
        self.set3 << self.data_Y["555"]
        self.set4 << self.data_Y["016"]

        self.bar_series = QPercentBarSeries()
        self.bar_series.append(self.set0)
        self.bar_series.append(self.set1)
        self.bar_series.append(self.set2)
        self.bar_series.append(self.set3)
        self.bar_series.append(self.set4)

    def selectionchange_occurences_Y(self, i):
        print("selection changed", self.comboBox_Y.currentText())
        self.this_data = self.data.dropna(subset=["LicensePlate","Barcode"], how="all")
        self.this_data = self.this_data.reset_index()
        self.this_data = self.this_data[["LicensePlate","Barcode", "Tunnel", "Source", "DestinationAirport", "ItemTime (local date)","Status", "PieceId"]]
        if self.comboBox_Y.currentText() == "noEDI":
            self.this_data = self.this_data[~self.this_data["Source"].isin(["EDI+EDI"])]
            self.this_data = self.this_data.reset_index()
            self.this_data = self.this_data[["LicensePlate","Barcode", "Tunnel", "Source", "DestinationAirport", "ItemTime (local date)","Status", "PieceId"]]
        
        self.airline_data = []
        self.airline_data_multi_occ = []
    
        for i in range(len(self.this_data["Barcode"])):
            string = str(self.this_data["Barcode"][i])
            if len(string) > 14:
                self.airline_data_multi_occ.append(self.this_data["Barcode"][i])
            if string=="nan":
                string = str(self.this_data["LicensePlate"][i])
                self.airline_data.append(string[1:4])
            else:
                self.airline_data.append(string[1:4])

        self.airline_data= pd.DataFrame(self.airline_data, columns=["AirlineData"])
        print(i)
        self.this_data["AirlineData"] = self.airline_data
        self.data_Y = self.this_data.groupby(["AirlineData","Source"])["AirlineData"].count()
        self.keys_Y = self.data_Y.keys()
        for i in range(len(data)):
            print(self.keys_Y[i], " : ", self.data_Y[i])
        self.update_bar()
            
    def selectionchange_occurences_X(self, i):
        print("selection changed", self.comboBox_X.currentText())
        self.str_data = self.frame[self.comboBox_X.currentText()].dropna()
        self.str_data = self.str_data.reset_index()
        self.str_data = self.str_data[self.comboBox_X.currentText()]

        self.airline_data = []
        self.airline_data_multi_occ = []
    
        for i in range(len(self.str_data)):
            string = str(self.str_data[i])
            if len(string) > 14:
                self.airline_data_multi_occ.append(self.str_data[i])
            else:
                self.airline_data.append(string[1:4])

        self.new_frame = pd.DataFrame(self.airline_data, columns=["AirlineData"])
        print(i)
        self.data_X = self.new_frame.groupby("AirlineData")["AirlineData"].count()
        self.keys_X = self.data.keys()
        for i in range(len(data)):
            print(self.keys_airline[i], " : ", self.data_airline[i])
        self.update_bar()


    def ocr(self):
        # OCR
        self.btn1 = QPushButton("OCR")
        self.btn1.clicked.connect(self.ocrbtn)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn4 = QCheckBox("EDI+OCR")
        self.btn4.setChecked(True)
        self.btn4.stateChanged.connect(lambda:self.btnstate_ocr(self.btn4))

        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItems(items)       
        self.comboBox1.activated[str].connect(self.comboBox1_logic)

        self.btn5 = QCheckBox("EDI+OCR+VCS")
        self.btn5.setChecked(True)
        self.btn5.stateChanged.connect(lambda:self.btnstate_ocr(self.btn5))


        self.comboBox2 = QComboBox(self)
        self.comboBox2.addItems(items)
        self.comboBox2.activated[str].connect(self.comboBox2_logic)

        self.btn6 = QCheckBox("OCR+EDI")
        self.btn6.setChecked(True)
        self.btn6.stateChanged.connect(lambda:self.btnstate_ocr(self.btn6))

        self.comboBox3 = QComboBox(self)
        self.comboBox3.addItems(items)
        self.comboBox3.activated[str].connect(self.comboBox3_logic)

        self.btn7 = QCheckBox("OCR+OCR")
        self.btn7.setChecked(True)
        self.btn7.stateChanged.connect(lambda:self.btnstate_ocr(self.btn7))

        self.comboBox4 = QComboBox(self)
        self.comboBox4.addItems(items)
        self.comboBox4.activated[str].connect(self.comboBox4_logic)

        self.btn8 = QCheckBox("OCR+VCS")
        self.btn8.setChecked(True)
        self.btn8.stateChanged.connect(lambda:self.btnstate_ocr(self.btn8))

        self.comboBox5 = QComboBox(self)
        self.comboBox5.addItems(items)
        self.comboBox5.activated[str].connect(self.comboBox5_logic)
    def vcs(self):
        self.btn2 = QPushButton("VCS")
        self.btn2.clicked.connect(self.vcsbtn)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn10 = QCheckBox("VCS")
        self.btn10.setChecked(True)

        self.comboBox6 = QComboBox(self)
        self.comboBox6.addItems(items)
        self.comboBox6.activated[str].connect(self.comboBox6_logic)

        self.btn11 = QCheckBox("VCS+VCS")
        self.btn11.setChecked(True)
        self.btn11.stateChanged.connect(lambda:self.btnstate_vcs(self.btn11))


        self.comboBox7 = QComboBox(self)
        self.comboBox7.addItems(items)
        self.comboBox7.activated[str].connect(self.comboBox7_logic)

        self.btn12 = QCheckBox("VCS+EDI")
        self.btn12.setChecked(True)

        self.comboBox8 = QComboBox(self)
        self.comboBox8.addItems(items)
        self.comboBox8.activated[str].connect(self.comboBox8_logic)

        self.btn13 = QCheckBox("EDI+VCS")
        self.btn13.setChecked(True)

        self.comboBox9 = QComboBox(self)
        self.comboBox9.addItems(items)
        self.comboBox9.activated[str].connect(self.comboBox9_logic)
    def mes(self):
        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]
        self.btn3 = QPushButton("MES")
        self.btn3.clicked.connect(self.mesbtn)

        self.btn14 = QCheckBox("VCS+VCS")
        self.btn14.setChecked(False)
        
        self.comboBox10 = QComboBox(self)
        self.comboBox10.addItems(items)
        self.comboBox10.activated[str].connect(self.comboBox10_logic)
    def edi(self):
        self.btn15 = QPushButton("EDI")
        self.btn15.clicked.connect(self.edibtn)

        self.btn16 = QCheckBox("EDI")
        self.btn16.setChecked(False)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        
        self.comboBox11 = QComboBox(self)
        self.comboBox11.addItems(items)
        self.comboBox11.activated[str].connect(self.comboBox11_logic)

        self.btn17 = QCheckBox("EDI+EDI")
        self.btn17.setChecked(False)

        self.comboBox12 = QComboBox(self)
        self.comboBox12.addItems(items)
        self.comboBox12.activated[str].connect(self.comboBox12_logic)

        self.btn18 = QCheckBox("EDI+EDI+EDI")
        self.btn18.setChecked(False)

        self.comboBox13 = QComboBox(self)
        self.comboBox13.addItems(items)
        self.comboBox13.activated[str].connect(self.comboBox13_logic)

    def add_layout(self):
        # add to the layout

        self.tab2.sublayout_up.addWidget(self.btn1)

        self.tab2.ocrlayout.addWidget(self.btn4)
        self.tab2.ocrlayout.addWidget(self.btn5)
        self.tab2.ocrlayout.addWidget(self.btn6)
        self.tab2.ocrlayout.addWidget(self.btn7)
        self.tab2.ocrlayout.addWidget(self.btn8)
        self.tab2.ocrlayout.addWidget(self.btn8)

        self.tab2.ocrcomb.addWidget(self.comboBox1)
        self.tab2.ocrcomb.addWidget(self.comboBox2)
        self.tab2.ocrcomb.addWidget(self.comboBox3)
        self.tab2.ocrcomb.addWidget(self.comboBox4)
        self.tab2.ocrcomb.addWidget(self.comboBox5)

        self.tab2.sublayout_down.addLayout( self.tab2.ocrlayout )
        self.tab2.sublayout_down.addLayout( self.tab2.ocrcomb )
        
        self.tab2.sublayout_up.addWidget( self.btn2 )
        self.tab2.vcslayout.addWidget( self.btn10)
        self.tab2.vcslayout.addWidget( self.btn11)
        self.tab2.vcslayout.addWidget( self.btn12)
        self.tab2.vcslayout.addWidget( self.btn13)

        self.tab2.vcscomb.addWidget(self.comboBox6)
        self.tab2.vcscomb.addWidget(self.comboBox7)
        self.tab2.vcscomb.addWidget(self.comboBox8)
        self.tab2.vcscomb.addWidget(self.comboBox9)

        self.tab2.sublayout_down.addLayout( self.tab2.vcslayout )
        self.tab2.sublayout_down.addLayout( self.tab2.vcscomb )

        self.tab2.sublayout_up.addWidget( self.btn3 )
        self.tab2.meslayout.addWidget( self.btn14 )

        self.tab2.mescomb.addWidget( self.comboBox10 )

        self.tab2.sublayout_down.addLayout( self.tab2.meslayout )
        self.tab2.sublayout_down.addLayout( self.tab2.mescomb )
    
        self.tab2.sublayout_up.addWidget( self.btn15 )
        self.tab2.edilayout.addWidget( self.btn16 )
        self.tab2.edilayout.addWidget( self.btn17 )
        self.tab2.edilayout.addWidget( self.btn18 )

        self.tab2.edicomb.addWidget( self.comboBox11 )
        self.tab2.edicomb.addWidget(self.comboBox12)
        self.tab2.edicomb.addWidget(self.comboBox13)

        self.tab2.sublayout_down.addLayout( self.tab2.edilayout )
        self.tab2.sublayout_down.addLayout( self.tab2.edicomb )
    def ocrbtn(self):
        self.btn4.setChecked(False)
        self.btn5.setChecked(False)
        self.btn6.setChecked(False)
        self.btn7.setChecked(False)
        self.btn8.setChecked(False)
        self.OCR_edi_ocr = 0
        self.OCR_edi_ocr = 0
        self.OCR_edi_ocr_vcs = 0
        self.OCR_ocr_edi = 0
        self.OCR_ocr_ocr = 0
        self.OCR_ocr_vcs = 0
        self.update_piechart()
    def vcsbtn(self):
        self.btn10.setChecked(False)
        self.btn11.setChecked(False)
        self.btn12.setChecked(False)
        self.btn13.setChecked(False)
        self.VCS_vcs = 0
        self.VCS_vcs_vcs = 0 
        self.VCS_vcs_edi = 0
        self.VCS_edi_vcs = 0
        self.update_piechart()
    def mesbtn(self):
        self.btn13.setChecked(False)
        self.MES_vcs_vcs = 0
        self.update_piechart()
    def edibtn(self):
        self.btn16.setChecked(False)
        self.btn17.setChecked(False)
        self.btn18.setChecked(False)
        self.EDI_edi = 0
        self.EDI_edi_edi = 0
        self.EDI_edi_edi_edi = 0
        self.update_piechart()
    def comboBox1_logic(self):
        print("selection changed", self.comboBox1.currentText())

        if self.comboBox1.currentText() == "Accept" or self.comboBox1.currentText() == "Reject" or self.comboBox1.currentText() == "Cancel":
            self.OCR_edi_ocr = self.status_count["EDI+OCR"][self.comboBox1.currentText()]
        else:
            self.OCR_edi_ocr = self.data_count[self.comboBox1.currentText()]["EDI+OCR"]
        self.update_piechart()
        print(self.OCR_edi_ocr)
    def comboBox2_logic(self):
        print("selection changed", self.comboBox2.currentText())

        if self.comboBox2.currentText() == "Accept" or self.comboBox2.currentText() == "Reject" or self.comboBox2.currentText() == "Cancel":
            self.OCR_edi_ocr_vcs = self.status_count["EDI+OCR+VCS"][self.comboBox2.currentText()]
        else:
            self.OCR_edi_ocr_vcs = self.data_count[self.comboBox2.currentText()]["EDI+OCR+VCS"]
        self.update_piechart()
        print(self.OCR_edi_ocr_vcs)
    def comboBox3_logic(self):
        print("selection changed", self.comboBox3.currentText())

        if self.comboBox3.currentText() == "Accept" or self.comboBox3.currentText() == "Reject" or self.comboBox3.currentText() == "Cancel":
            self.OCR_ocr_edi = self.status_count["OCR+EDI"][self.comboBox3.currentText()]
        else:
            self.OCR_ocr_edi = self.data_count[self.comboBox3.currentText()]["OCR+EDI"]
        self.update_piechart()
        print(self.OCR_ocr_edi)
    def comboBox4_logic(self):
        print("selection changed", self.comboBox4.currentText())

        if self.comboBox4.currentText() == "Accept" or self.comboBox4.currentText() == "Reject" or self.comboBox4.currentText() == "Cancel":
            self.OCR_ocr_ocr = self.status_count["OCR+OCR"][self.comboBox4.currentText()]
        else:
            self.OCR_ocr_ocr = self.data_count[self.comboBox4.currentText()]["OCR+OCR"]
        self.update_piechart()
        print(self.OCR_ocr_ocr)
    def comboBox5_logic(self):
        print("selection changed", self.comboBox5.currentText())

        if self.comboBox5.currentText() == "Accept" or self.comboBox5.currentText() == "Reject" or self.comboBox5.currentText() == "Cancel":
            self.OCR_ocr_vcs = self.status_count["OCR+VCS"][self.comboBox5.currentText()]
        else:
            self.OCR_ocr_vcs = self.data_count[self.comboBox5.currentText()]["OCR+VCS"]
        self.update_piechart()
        print(self.OCR_ocr_vcs)
    def comboBox6_logic(self):
        print("selection changed", self.comboBox6.currentText())

        if self.comboBox6.currentText() == "Accept" or self.comboBox6.currentText() == "Reject" or self.comboBox6.currentText() == "Cancel":
            self.VCS_vcs = self.status_count["VCS"][self.comboBox6.currentText()]
        else:
            self.VCS_vcs = self.data_count[self.comboBox6.currentText()]["VCS"]
        self.update_piechart()
        print(self.VCS_vcs)
    def comboBox7_logic(self):
        print("selection changed", self.comboBox7.currentText())

        if self.comboBox7.currentText() == "Accept" or self.comboBox7.currentText() == "Reject" or self.comboBox7.currentText() == "Cancel":
            self.VCS_vcs_vcs = self.status_count["VCS+VCS"][self.comboBox7.currentText()]
        else:
            self.VCS_vcs_vcs = self.data_count[self.comboBox7.currentText()]["VCS+VCS"]
        self.update_piechart()
        print(self.VCS_vcs_vcs)
    def comboBox8_logic(self):
        print("selection changed", self.comboBox8.currentText())

        if self.comboBox8.currentText() == "Accept" or self.comboBox8.currentText() == "Reject" or self.comboBox8.currentText() == "Cancel":
            self.VCS_vcs_edi = self.status_count["VCS+EDI"][self.comboBox8.currentText()]
        else:
            self.VCS_vcs_edi = self.data_count[self.comboBox8.currentText()]["VCS+EDI"]
        self.update_piechart()
        print(self.VCS_vcs_edi)
    def comboBox9_logic(self):
        print("selection changed", self.comboBox9.currentText())

        if self.comboBox9.currentText() == "Accept" or self.comboBox9.currentText() == "Reject" or self.comboBox9.currentText() == "Cancel":
            self.VCS_edi_vcs = self.status_count["EDI+VCS"][self.comboBox9.currentText()]
        else:
            self.VCS_edi_vcs = self.data_count[self.comboBox9.currentText()]["EDI+VCS"]
        self.update_piechart()
        print(self.VCS_edi_vcs)
    def comboBox10_logic(self):
        print("selection changed", self.comboBox10.currentText())

        if self.comboBox10.currentText() == "Accept" or self.comboBox10.currentText() == "Reject" or self.comboBox10.currentText() == "Cancel":
            self.MES_vcs_vcs = self.status_count["VCS+VCS"][self.comboBox10.currentText()]
        else:
            self.MES_vcs_vcs = self.data_count[self.comboBox10.currentText()]["VCS+VCS"]
        self.update_piechart()
        print(self.MES_vcs_vcs)
    def comboBox11_logic(self):
        print("selection changed", self.comboBox11.currentText())

        if self.comboBox11.currentText() == "Accept" or self.comboBox11.currentText() == "Reject" or self.comboBox11.currentText() == "Cancel":
            self.EDI_edi = self.status_count["EDI"][self.comboBox11.currentText()]
        else:
            self.EDI_edi = self.data_count[self.comboBox11.currentText()]["EDI"]
        self.update_piechart()
        print(self.EDI_edi)
    def comboBox12_logic(self):
        print("selection changed", self.comboBox12.currentText())

        if self.comboBox12.currentText() == "Accept" or self.comboBox12.currentText() == "Reject" or self.comboBox12.currentText() == "Cancel":
            self.EDI_edi_edi = self.status_count["EDI+EDI"][self.comboBox12.currentText()]
        else:
            self.EDI_edi_edi = self.data_count[self.comboBox12.currentText()]["EDI+EDI"]
        self.update_piechart()
        print(self.EDI_edi_edi)
    def comboBox13_logic(self):
        print("selection changed", self.comboBox13.currentText())

        if self.comboBox13.currentText() == "Accept" or self.comboBox13.currentText() == "Reject" or self.comboBox13.currentText() == "Cancel":
            self.EDI_edi_edi_edi = self.status_count["EDI+EDI+EDI"][self.comboBox13.currentText()]
        else:
            self.EDI_edi_edi_edi = self.data_count[self.comboBox13.currentText()]["EDI+EDI+EDI"]
        self.update_piechart()
        print(self.EDI_edi_edi_edi)
class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

class CustomDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Data Folder")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

def main2():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main2()