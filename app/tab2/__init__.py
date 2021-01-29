from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class tab2():
    def __init__(self):
        # buckets
        self.bucket1 = QLabel()
        self.bucket1.setAlignment(Qt.AlignCenter)
        #OCR
        self.ocr(False)
        #VCS
        self.vcs(False)
        #EDI
        self.edi(False)
        #MES
        self.mes(False)

    def ocr(self, state):
        self.btn1 = QPushButton("OCR")

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn4 = QCheckBox("EDI+OCR")
        self.btn4.setChecked(state)

        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(items)       

        self.btn5 = QCheckBox("EDI+OCR+VCS")
        self.btn5.setChecked(state)

        self.comboBox2 = QComboBox()
        self.comboBox2.addItems(items)

        self.btn6 = QCheckBox("OCR+EDI")
        self.btn6.setChecked(state)

        self.comboBox3 = QComboBox()
        self.comboBox3.addItems(items)

        self.btn7 = QCheckBox("OCR+OCR")
        self.btn7.setChecked(state)

        self.comboBox4 = QComboBox()
        self.comboBox4.addItems(items)

        self.btn8 = QCheckBox("OCR+VCS")
        self.btn8.setChecked(state)

        self.comboBox5 = QComboBox()
        self.comboBox5.addItems(items)
    
    def vcs(self, state):
        self.btn2 = QPushButton("VCS")

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        self.btn10 = QCheckBox("VCS")
        self.btn10.setChecked(state)

        self.comboBox6 = QComboBox()
        self.comboBox6.addItems(items)

        self.btn11 = QCheckBox("VCS+VCS")
        self.btn11.setChecked(state)

        self.comboBox7 = QComboBox()
        self.comboBox7.addItems(items)

        self.btn12 = QCheckBox("VCS+EDI")
        self.btn12.setChecked(state)

        self.comboBox8 = QComboBox()
        self.comboBox8.addItems(items)

        self.btn13 = QCheckBox("EDI+VCS")
        self.btn13.setChecked(state)

        self.comboBox9 = QComboBox()
        self.comboBox9.addItems(items)

    def mes(self, state):
        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]
        self.btn3 = QPushButton("MES")

        self.btn14 = QCheckBox("VCS+VCS")
        self.btn14.setChecked(state)
        
        self.comboBox10 = QComboBox()
        self.comboBox10.addItems(items)

    def edi(self, state):
        self.btn15 = QPushButton("EDI")

        self.btn16 = QCheckBox("EDI")
        self.btn16.setChecked(state)

        items = ["Barcode", "LicensePlate", "PieceId", "Accept", "Cancel", "Reject"]

        
        self.comboBox11 = QComboBox()
        self.comboBox11.addItems(items)

        self.btn17 = QCheckBox("EDI+EDI")
        self.btn17.setChecked(state)

        self.comboBox12 = QComboBox()
        self.comboBox12.addItems(items)

        self.btn18 = QCheckBox("EDI+EDI+EDI")
        self.btn18.setChecked(state)

        self.comboBox13 = QComboBox()
        self.comboBox13.addItems(items)