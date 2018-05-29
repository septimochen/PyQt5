#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

This program creates a menubar. The
menubar has one menu with an exit action.

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Simple Menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



