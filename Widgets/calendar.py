#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This example shows a QCalendarWidget widget.

"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout(self)

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)

        self.vbox.addWidget(self.cal)

        self.lbl = QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())

        self.vbox.addWidget(self.lbl)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
