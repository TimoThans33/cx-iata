from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class tab2():
    def __init__(self):
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

        #OCR
        self.ocr()
        #VCS
        self.vcs()
        #EDI
        self.edi()
        #MES
        self.mes()

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

        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

    def ocr(self):
        self.btn1 = QPushButton("OCR")
        self.btn1.clicked.connect(self.ocrbtn)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn4 = QCheckBox("EDI+OCR")
        self.btn4.setChecked(True)
        self.btn4.stateChanged.connect(lambda:self.btnstate_ocr(self.btn4))

        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(items)       
        self.comboBox1.activated[str].connect(self.comboBox1_logic)

        self.btn5 = QCheckBox("EDI+OCR+VCS")
        self.btn5.setChecked(True)
        self.btn5.stateChanged.connect(lambda:self.btnstate_ocr(self.btn5))


        self.comboBox2 = QComboBox()
        self.comboBox2.addItems(items)
        self.comboBox2.activated[str].connect(self.comboBox2_logic)

        self.btn6 = QCheckBox("OCR+EDI")
        self.btn6.setChecked(True)
        self.btn6.stateChanged.connect(lambda:self.btnstate_ocr(self.btn6))

        self.comboBox3 = QComboBox()
        self.comboBox3.addItems(items)
        self.comboBox3.activated[str].connect(self.comboBox3_logic)

        self.btn7 = QCheckBox("OCR+OCR")
        self.btn7.setChecked(True)
        self.btn7.stateChanged.connect(lambda:self.btnstate_ocr(self.btn7))

        self.comboBox4 = QComboBox()
        self.comboBox4.addItems(items)
        self.comboBox4.activated[str].connect(self.comboBox4_logic)

        self.btn8 = QCheckBox("OCR+VCS")
        self.btn8.setChecked(True)
        self.btn8.stateChanged.connect(lambda:self.btnstate_ocr(self.btn8))

        self.comboBox5 = QComboBox()
        self.comboBox5.addItems(items)
        self.comboBox5.activated[str].connect(self.comboBox5_logic)
    
    def vcs(self):
        self.btn2 = QPushButton("VCS")
        self.btn2.clicked.connect(self.vcsbtn)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn10 = QCheckBox("VCS")
        self.btn10.setChecked(True)
        self.btn10.stateChanged.connect(lambda:self.btnstate_vcs(self.btn10))

        self.comboBox6 = QComboBox()
        self.comboBox6.addItems(items)
        self.comboBox6.activated[str].connect(self.comboBox6_logic)

        self.btn11 = QCheckBox("VCS+VCS")
        self.btn11.setChecked(True)
        self.btn11.stateChanged.connect(lambda:self.btnstate_vcs(self.btn11))


        self.comboBox7 = QComboBox()
        self.comboBox7.addItems(items)
        self.comboBox7.activated[str].connect(self.comboBox7_logic)

        self.btn12 = QCheckBox("VCS+EDI")
        self.btn12.setChecked(True)
        self.btn12.stateChanged.connect(lambda:self.btnstate_vcs(self.btn12))

        self.comboBox8 = QComboBox()
        self.comboBox8.addItems(items)
        self.comboBox8.activated[str].connect(self.comboBox8_logic)

        self.btn13 = QCheckBox("EDI+VCS")
        self.btn13.setChecked(True)
        self.btn13.stateChanged.connect(lambda:self.btnstate_vcs(self.btn13))

        self.comboBox9 = QComboBox()
        self.comboBox9.addItems(items)
        self.comboBox9.activated[str].connect(self.comboBox9_logic)

    def mes(self):
        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]
        self.btn3 = QPushButton("MES")
        self.btn3.clicked.connect(self.mesbtn)

        self.btn14 = QCheckBox("VCS+VCS")
        self.btn14.setChecked(False)
        
        self.comboBox10 = QComboBox()
        self.comboBox10.addItems(items)
        self.comboBox10.activated[str].connect(self.comboBox10_logic)

    def edi(self):
        self.btn15 = QPushButton("EDI")
        self.btn15.clicked.connect(self.edibtn)

        self.btn16 = QCheckBox("EDI")
        self.btn16.setChecked(False)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        
        self.comboBox11 = QComboBox()
        self.comboBox11.addItems(items)
        self.comboBox11.activated[str].connect(self.comboBox11_logic)

        self.btn17 = QCheckBox("EDI+EDI")
        self.btn17.setChecked(False)

        self.comboBox12 = QComboBox()
        self.comboBox12.addItems(items)
        self.comboBox12.activated[str].connect(self.comboBox12_logic)

        self.btn18 = QCheckBox("EDI+EDI+EDI")
        self.btn18.setChecked(False)

        self.comboBox13 = QComboBox()
        self.comboBox13.addItems(items)
        self.comboBox13.activated[str].connect(self.comboBox13_logic)

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
    def vcsbtn(self):
        self.btn10.setChecked(False)
        self.btn11.setChecked(False)
        self.btn12.setChecked(False)
        self.btn13.setChecked(False)
        self.VCS_vcs = 0
        self.VCS_vcs_vcs = 0 
        self.VCS_vcs_edi = 0
        self.VCS_edi_vcs = 0
    def mesbtn(self):
        self.btn13.setChecked(False)
        self.MES_vcs_vcs = 0
    def edibtn(self):
        self.btn16.setChecked(False)
        self.btn17.setChecked(False)
        self.btn18.setChecked(False)
        self.EDI_edi = 0
        self.EDI_edi_edi = 0
        self.EDI_edi_edi_edi = 0
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

    def btnstate_edi(self, b):
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

    def btnstate_mes(self, b):
        if b.text() == "MES_vcs_vcs":
            if b.isChecked() == True:
                self.MES_vcs = 0
                print(b.text(),"is selected")
            else:
                print(b.text(),"is deselected")


    def comboBox1_logic(self):
        print("selection changed", self.comboBox1.currentText())

        if self.comboBox1.currentText() == "Accept" or self.comboBox1.currentText() == "Reject" or self.comboBox1.currentText() == "Cancel":
            self.OCR_edi_ocr = self.status_count["EDI+OCR"][self.comboBox1.currentText()]
        else:
            self.OCR_edi_ocr = self.data_count[self.comboBox1.currentText()]["EDI+OCR"]
        print(self.OCR_edi_ocr)
    def comboBox2_logic(self):
        print("selection changed", self.comboBox2.currentText())

        if self.comboBox2.currentText() == "Accept" or self.comboBox2.currentText() == "Reject" or self.comboBox2.currentText() == "Cancel":
            self.OCR_edi_ocr_vcs = self.status_count["EDI+OCR+VCS"][self.comboBox2.currentText()]
        else:
            self.OCR_edi_ocr_vcs = self.data_count[self.comboBox2.currentText()]["EDI+OCR+VCS"]
        print(self.OCR_edi_ocr_vcs)
    def comboBox3_logic(self):
        print("selection changed", self.comboBox3.currentText())

        if self.comboBox3.currentText() == "Accept" or self.comboBox3.currentText() == "Reject" or self.comboBox3.currentText() == "Cancel":
            self.OCR_ocr_edi = self.status_count["OCR+EDI"][self.comboBox3.currentText()]
        else:
            self.OCR_ocr_edi = self.data_count[self.comboBox3.currentText()]["OCR+EDI"]
        print(self.OCR_ocr_edi)
    def comboBox4_logic(self):
        print("selection changed", self.comboBox4.currentText())

        if self.comboBox4.currentText() == "Accept" or self.comboBox4.currentText() == "Reject" or self.comboBox4.currentText() == "Cancel":
            self.OCR_ocr_ocr = self.status_count["OCR+OCR"][self.comboBox4.currentText()]
        else:
            self.OCR_ocr_ocr = self.data_count[self.comboBox4.currentText()]["OCR+OCR"]
        print(self.OCR_ocr_ocr)
    def comboBox5_logic(self):
        print("selection changed", self.comboBox5.currentText())

        if self.comboBox5.currentText() == "Accept" or self.comboBox5.currentText() == "Reject" or self.comboBox5.currentText() == "Cancel":
            self.OCR_ocr_vcs = self.status_count["OCR+VCS"][self.comboBox5.currentText()]
        else:
            self.OCR_ocr_vcs = self.data_count[self.comboBox5.currentText()]["OCR+VCS"]
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

