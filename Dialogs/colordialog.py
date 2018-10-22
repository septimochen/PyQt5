#!/usr/bin/python3
# -*- coding: utf-8 -*-
#color dialog

"""

In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget.

"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(400, 22, 200, 200)

        self.setGeometry(777, 555, 670, 449)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
