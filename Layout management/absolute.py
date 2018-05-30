#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows three labels on a window
using absolute positioning.

"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('NBA', self)
        label1.move(10, 20)

        label2 = QLabel("This is why we play!", self)
        label2.move(40, 50)

        label3 = QLabel('Playoffs 2018', self)
        label3.move(70, 80)

        self.setGeometry(600, 600, 320, 240)
        self.setWindowTitle('NBA')
        self.setWindowIcon(QIcon('nba.jpg'))
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

