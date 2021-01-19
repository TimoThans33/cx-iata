class CreateTab1():
    def __init__(self):
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

