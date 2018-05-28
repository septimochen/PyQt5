"""
ZetCode PyQt5 tutorial

This program creates a quit
button. When we press the button,
the application terminates.

"""
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(60, 60)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Dota 2')
        self.setWindowIcon(QIcon('dota_2.png'))

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
