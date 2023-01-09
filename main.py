# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtCore
from mainwindow import MainWindow


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()


    sys.exit(app.exec_())
