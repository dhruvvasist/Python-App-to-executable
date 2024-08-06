import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 400, 400)
    win.setWindowTitle("Sample App")
    win.setWindowIcon(QIcon("Cover 8.jpg"))
    win.show()
    sys.exit(app.exec_())


window()
