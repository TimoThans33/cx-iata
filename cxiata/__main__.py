from cxiata import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    