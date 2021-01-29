from PyQt5.QtWidgets import QPushButton, QProgressBar
import pyqtgraph as pg

class tab1():
    def __init__(self):
        # folder button
        self.btn = QPushButton("Folder")
        self.btn.adjustSize()
        # progress bar
        self.progress = QProgressBar()
        self.progress.adjustSize()
        # graph
        self.graphWidget = pg.PlotWidget()
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
        self.graphWidget.setYRange(0, 55000, padding=0)

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
