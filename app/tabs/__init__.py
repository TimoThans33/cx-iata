from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from glob import glob
import numpy as np
import pandas as pd

from app.tab1 import *
from app.tab2 import *
from app.tab3 import *

class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize list
        self.data_count = 0
        self.main_tab2_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

        # Initialize the tab screens
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab1_lib = tab1()

        self.tab2 = QWidget()
        self.tab2_lib = tab2()

        # self.tab3 = QWidget()
        # self.tab3_lib = tab3()
        self.tabs.resize(600, 400)

        # adding tabs
        self.tabs.addTab(self.tab1, "Activity")
        self.tabs.addTab(self.tab2, "Overview")
        # self.tabs.addTab(self.tab3, "Advanced")

        # create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.tab1_lib.btn)
        self.tab1_lib.btn.clicked.connect(self.getDirectories)

        self.tab1.layout.addWidget(self.tab1_lib.progress)
        self.tab1.layout.addWidget(self.tab1_lib.graphWidget)
        self.tab1.setLayout(self.tab1.layout)

        # create second tab
        self.tab2.layout = QVBoxLayout(self)

        self.update_piechart()
        self.initPie()
        
        # buckets
        self.tab2.layout.addWidget(self.tab2_lib.bucket1)

        #pie chart
        self.tab2.layout.addWidget(self.chartview)

        self.tab2.sublayout_up = QHBoxLayout(self)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn1)
        self.tab2_lib.btn1.clicked.connect(self.ocrbtn)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn2)
        self.tab2_lib.btn2.clicked.connect(self.vcsbtn)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn15)
        self.tab2_lib.btn15.clicked.connect(self.edibtn)
        self.tab2.sublayout_up.addWidget(self.tab2_lib.btn3)
        self.tab2_lib.btn3.clicked.connect(self.mesbtn)        
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

        # create third tab
        # self.tab3.layout = QVBoxLayout(self)
        # self.tab3.layout.addWidget(self.tab3_lib.comboBox_Y)
        # self.tab3_lib.comboBox_Y.activated[str].connect(self.selectionchange_occurences_Y)
        # self.tab3.layout.addWidget(self.tab3_lib.chartView)
        
        # self.tab3.setLayout(self.tab3.layout)

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
            self.tab1_lib.progress.setValue(self.completed)
        self.tab1_lib.progress.setValue(100)
        self.frame = pd.concat(self.li, axis=0, ignore_index=True)
        # read usefull data
        self.data = self.frame[["LicensePlate","Barcode", "Tunnel", "Source", "DestinationAirport", "ItemTime (local date)","Status", "PieceId"]]
        # show dates in plot
        self.dates = self.data.groupby(["ItemTime (local date)"])["PieceId"].count()
        self.keys = self.dates.keys()
        self.tab1_lib.plot(np.linspace(0, 10, len(self.dates)), self.dates, "activity", 'r')

        # process data
        self.data_count = self.data.groupby(["Source"]).count()
        self.status_count = self.data.groupby(["Source","Status"])["PieceId"].count()
    
    def ocrToLayout(self):
        self.tab2.ocrlayout = QVBoxLayout(self)

        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn4)
        self.tab2_lib.btn4.stateChanged.connect(lambda:self.btnstate_ocr(self.tab2_lib.btn4))
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn5)
        self.tab2_lib.btn5.stateChanged.connect(lambda:self.btnstate_ocr(self.tab2_lib.btn5))
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn6)
        self.tab2_lib.btn6.stateChanged.connect(lambda:self.btnstate_ocr(self.tab2_lib.btn6))
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn7)
        self.tab2_lib.btn7.stateChanged.connect(lambda:self.btnstate_ocr(self.tab2_lib.btn7))
        self.tab2.ocrlayout.addWidget(self.tab2_lib.btn8)
        self.tab2_lib.btn8.stateChanged.connect(lambda:self.btnstate_ocr(self.tab2_lib.btn8))

        self.tab2.sublayout_down.addLayout( self.tab2.ocrlayout )

        self.tab2.ocrcomb = QVBoxLayout(self)

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox1)
        self.tab2_lib.comboBox1.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn4, self.tab2_lib.comboBox1.currentText(), "EDI+OCR", self.main_tab2_list, 0))

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox2)
        self.tab2_lib.comboBox2.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn5, self.tab2_lib.comboBox2.currentText(), "EDI+OCR+VCS", self.main_tab2_list, 1))

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox3)
        self.tab2_lib.comboBox3.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn6, self.tab2_lib.comboBox3.currentText(), "OCR+EDI", self.main_tab2_list, 2))

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox4)
        self.tab2_lib.comboBox4.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn7, self.tab2_lib.comboBox4.currentText(), "OCR+OCR", self.main_tab2_list, 3))

        self.tab2.ocrcomb.addWidget(self.tab2_lib.comboBox5)
        self.tab2_lib.comboBox5.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn8, self.tab2_lib.comboBox5.currentText(), "OCR+VCS", self.main_tab2_list, 4))

        self.tab2.sublayout_down.addLayout( self.tab2.ocrcomb )

    def vcsToLayout(self):
        self.tab2.vcslayout = QVBoxLayout(self)

        self.tab2.vcslayout.addWidget(self.tab2_lib.btn10)
        self.tab2_lib.btn10.stateChanged.connect(lambda:self.btnstate_vcs(self.tab2_lib.btn10))
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn11)
        self.tab2_lib.btn11.stateChanged.connect(lambda:self.btnstate_vcs(self.tab2_lib.btn11))
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn12)
        self.tab2_lib.btn12.stateChanged.connect(lambda:self.btnstate_vcs(self.tab2_lib.btn12))
        self.tab2.vcslayout.addWidget(self.tab2_lib.btn13)
        self.tab2_lib.btn13.stateChanged.connect(lambda:self.btnstate_vcs(self.tab2_lib.btn13))

        self.tab2.sublayout_down.addLayout( self.tab2.vcslayout )

        self.tab2.vcscomb = QVBoxLayout(self)

        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox6 )
        self.tab2_lib.comboBox6.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn10, self.tab2_lib.comboBox6.currentText(), "VCS", self.main_tab2_list, 5))
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox7 )
        self.tab2_lib.comboBox7.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn11, self.tab2_lib.comboBox7.currentText(), "VCS+VCS", self.main_tab2_list, 6))
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox8 )
        self.tab2_lib.comboBox8.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn12, self.tab2_lib.comboBox8.currentText(), "VCS+EDI", self.main_tab2_list, 7))
        self.tab2.vcscomb.addWidget( self.tab2_lib.comboBox9 )
        self.tab2_lib.comboBox9.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn13, self.tab2_lib.comboBox9.currentText(), "EDI+VCS", self.main_tab2_list, 8))
        self.tab2.sublayout_down.addLayout( self.tab2.vcscomb )

    def ediToLayout(self):
        self.tab2.edilayout = QVBoxLayout(self)

        self.tab2.edilayout.addWidget(self.tab2_lib.btn16)
        self.tab2_lib.btn16.stateChanged.connect(lambda:self.btnstate_edi(self.tab2_lib.btn16))
        self.tab2.edilayout.addWidget(self.tab2_lib.btn17)
        self.tab2_lib.btn17.stateChanged.connect(lambda:self.btnstate_edi(self.tab2_lib.btn17))
        self.tab2.edilayout.addWidget(self.tab2_lib.btn18)
        self.tab2_lib.btn18.stateChanged.connect(lambda:self.btnstate_edi(self.tab2_lib.btn18))
        self.tab2.sublayout_down.addLayout( self.tab2.edilayout )

        self.tab2.edicomb = QVBoxLayout(self)

        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox11)
        self.tab2_lib.comboBox11.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn16, self.tab2_lib.comboBox11.currentText(), "EDI", self.main_tab2_list, 9))
        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox12)
        self.tab2_lib.comboBox12.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn17, self.tab2_lib.comboBox12.currentText(), "EDI+EDI", self.main_tab2_list, 10))
        self.tab2.edicomb.addWidget(self.tab2_lib.comboBox13)
        self.tab2_lib.comboBox13.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn18, self.tab2_lib.comboBox13.currentText(), "EDI+EDI+EDI", self.main_tab2_list, 11))
        self.tab2.sublayout_down.addLayout( self.tab2.edicomb )

    def mesToLayout(self):
        self.tab2.meslayout = QVBoxLayout(self)

        self.tab2.meslayout.addWidget(self.tab2_lib.btn14)
        self.tab2_lib.btn14.stateChanged.connect(lambda:self.btnstate_edi(self.tab2_lib.btn14))
        self.tab2.sublayout_down.addLayout( self.tab2.meslayout )

        self.tab2.mescomb = QVBoxLayout(self)
        
        self.tab2.mescomb.addWidget( self.tab2_lib.comboBox10 )
        self.tab2_lib.comboBox10.activated[str].connect(lambda:self.comboBox_logic(self.tab2_lib.btn14, self.tab2_lib.comboBox10.currentText(), "VCS+VCS", self.main_tab2_list, 12))
        self.tab2.sublayout_down.addLayout( self.tab2.mescomb )

    def selectionchange_occurences_Y(self, i):
        print("selection changed", self.tab3_lib.comboBox_Y.currentText())
        self.this_data = self.data.dropna(subset=["LicensePlate","Barcode"], how="all")
        self.this_data = self.this_data.reset_index()
        self.this_data = self.this_data[["LicensePlate","Barcode", "Tunnel", "Source", "DestinationAirport", "ItemTime (local date)","Status", "PieceId"]]
        if self.tab3_lib.comboBox_Y.currentText() == "noEDI":
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

    def comboBox_logic(self, b, text, string, list, count):
        if b.isChecked() == True:
            print("selection changed", text)
            if text == "Accept" or text == "Reject" or text == "Cancel":
                list[count] = self.status_count[string][text]
            if text == "Barcode" or text == "LicensePlate" or text == "PieceId":
                list[count] = self.data_count[text][string]
            self.update_piechart()
            print(list[count])

    def initPie(self):

        slice = QPieSlice()
        slice = self.series.slices()[3]
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

        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)


    def ocrbtn(self):
        self.tab2_lib.btn4.setChecked(False)
        self.tab2_lib.btn5.setChecked(False)
        self.tab2_lib.btn6.setChecked(False)
        self.tab2_lib.btn7.setChecked(False)
        self.tab2_lib.btn8.setChecked(False)
        self.main_tab2_list[0:4] = [0, 0, 0, 0, 0]
        self.update_piechart()

    def vcsbtn(self):
        self.tab2_lib.btn10.setChecked(False)
        self.tab2_lib.btn11.setChecked(False)
        self.tab2_lib.btn12.setChecked(False)
        self.tab2_lib.btn13.setChecked(False)
        self.main_tab2_list[5:8] = [0, 0, 0, 0]
        self.update_piechart()
    def mesbtn(self):
        self.tab2_lib.btn13.setChecked(False)
        self.main_tab2_list[12] = 0
        self.update_piechart()
    def edibtn(self):
        self.tab2_lib.btn16.setChecked(False)
        self.tab2_lib.btn17.setChecked(False)
        self.tab2_lib.btn18.setChecked(False)
        self.main_tab2_list[9:11] = [0, 0, 0]
        self.update_piechart()

    def btnstate_ocr(self, b):
        if b.text() == "EDI+OCR":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn4, self.tab2_lib.comboBox1.currentText(), "EDI+OCR", self.main_tab2_list, 0)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[0] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "EDI+OCR+VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn5, self.tab2_lib.comboBox2.currentText(), "EDI+OCR+VCS", self.main_tab2_list, 1)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[1] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "OCR+EDI":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn6, self.tab2_lib.comboBox3.currentText(), "OCR+EDI", self.main_tab2_list, 2)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[2] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "OCR+OCR":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn7, self.tab2_lib.comboBox4.currentText(), "OCR+OCR", self.main_tab2_list, 3)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[3] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "OCR+VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn8, self.tab2_lib.comboBox5.currentText(), "OCR+VCS", self.main_tab2_list, 4)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[4] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
    def btnstate_vcs(self, b):
        if b.text() == "VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn10, self.tab2_lib.comboBox6.currentText(), "VCS", self.main_tab2_list, 5)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[5] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "VCS+VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn11, self.tab2_lib.comboBox7.currentText(), "VCS+VCS", self.main_tab2_list, 6)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[6] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "VCS+EDI":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn12, self.tab2_lib.comboBox8.currentText(), "VCS+EDI", self.main_tab2_list, 7)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[7] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "EDI+VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn13, self.tab2_lib.comboBox9.currentText(), "EDI+VCS", self.main_tab2_list, 8)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[8] = 0
                self.update_piechart()
                print(b.text(),"is deselected")

    def btnstate_edi(self, b):
        if b.text() == "EDI":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn16, self.tab2_lib.comboBox11.currentText(), "EDI", self.main_tab2_list, 9)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[9] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "EDI+EDI":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn17, self.tab2_lib.comboBox12.currentText(), "EDI+EDI", self.main_tab2_list, 10)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[10] = 0
                self.update_piechart()
                print(b.text(),"is deselected")
        if b.text() == "EDI+EDI+EDI":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn18, self.tab2_lib.comboBox13.currentText(), "EDI+EDI+EDI", self.main_tab2_list, 11)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[11] = 0
                self.update_piechart()
                print(b.text(),"is deselected")

    def btnstate_mes(self, b):
        if b.text() == "VCS+VCS":
            if b.isChecked() == True:
                self.comboBox_logic(self.tab2_lib.btn14, self.tab2_lib.comboBox10.currentText(), "VCS+VCS", self.main_tab2_list, 12)
                self.update_piechart()
                print(b.text(),"is selected")
            else:
                self.main_tab2_list[12] = 0
                self.update_piechart()
                print(b.text(),"is deselected")

    def update_piechart(self):
        self.OCR = sum(self.main_tab2_list[0:4]) # self.OCR_edi_ocr + self.OCR_edi_ocr_vcs + self.OCR_ocr_edi + self.OCR_ocr_ocr + self.OCR_ocr_vcs
        self.VCS = sum(self.main_tab2_list[5:8]) # self.VCS_vcs + self.VCS_vcs_vcs + self.VCS_vcs_edi + self.VCS_edi_vcs
        self.EDI = sum(self.main_tab2_list[9:11]) # self.MES_vcs_vcs
        self.MES = self.main_tab2_list[12] # self.EDI_edi + self.EDI_edi_edi + self.EDI_edi_edi_edi

        self.series.clear()

        self.series.append("OCR", self.OCR)
        self.series.append("VCS", self.VCS)
        self.series.append("MES", self.MES)
        self.series.append("EDI", self.EDI)

        print("OCR",self.OCR,"VCS", self.VCS,"MES",self.MES,"EDI",self.EDI)
        self.tab2_lib.bucket1.setText("OCR {:d} VCS {:d} MES {:d} EDI {:d}".format(self.OCR, self.VCS, self.MES, self.EDI))
        # print("OCR",self.main_tab2_list,"VCS", self.main_tab2_list,"MES",self.main_tab2_list,"EDI",self.main_tab2_list)
