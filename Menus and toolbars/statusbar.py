"""

-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'statusbar.py'

Created by: PyQt5 UI code generator 5.6

WARNING! All changes made in this file will be lost!


"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Status Bar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


