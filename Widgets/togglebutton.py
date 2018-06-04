#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In this example, we create three toggle buttons.
They will control the background color of a
QFrame.
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFrame
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(30, 30)
        redb.clicked.connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(30, 130)
        blueb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(30, 230)
        greenb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(250, 30, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle('Toggle Button')
        self.show()


    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

