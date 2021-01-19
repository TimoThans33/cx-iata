class CreateTab2():
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
        # Series for PieChart
        self.seris = QPieSeries()
        # ocr
        self.ocr()
        # vcs
        self.vcs()
        # mes
        self.mes()
        # edi
        self.edi()

        self.add_layout()
        self.update_piechart()

        self.create_piechart()
        
        self.tab2.layout.addWidget(chartview)

        self.sl = QSlider(Qt.Horizontal, self)
        self.sl.valueChanged[int].connect(self.valuechange)

        self.tab2.layout.addWidget(self.sl)

    def create_piechart(self):
        # adding slices
        slice = QPieSlice()
        slice = self.series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)

        # creating the chart
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