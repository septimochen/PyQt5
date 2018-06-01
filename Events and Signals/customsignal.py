#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we show how to
emit a custom signal.
"""
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(400, 400, 440, 320)
        self.setWindowTitle("Emit Signal")
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
