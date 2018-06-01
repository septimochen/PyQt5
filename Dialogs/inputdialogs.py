#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we receive data from
a QInputDialog dialog.

"""

import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QPushButton, QLineEdit, QInputDialog)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Input', self)
        self.btn.move(150, 50)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle('Dialog of Dota2')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')

        if ok:
            self.le.setText(text)


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
