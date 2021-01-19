from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class tab3():
    def __init__(self):
        items = ["noEDI", "EDI"]
        self.comboBox_Y = QComboBox()

        self.comboBox_Y.addItems(items)

        self.comboBox_Y.adjustSize()
        #self.tab3.layout.addWidget(self.comboBox_Y)
        #self.comboBox_Y.activated[str].connect(self.selectionchange_occurences_Y)

        self.create_bar()

    def create_bar(self):
        # The QBarSet class represents a set of bars

        self.set0 = QBarSet("OCR")
        self.set1 = QBarSet("EDI")
        self.set2 = QBarSet("VCS")
        self.set3 = QBarSet("MES")
        self.set4 = QBarSet("VCS2")

        #dummy data
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