class App(QMainWindow):
    def __init__(self):
        super().__init__()
        # main window
        self.setWindowTitle('Iata analyses')
        self.setGeometry(50, 50, 1000, 1000)

        self.show()