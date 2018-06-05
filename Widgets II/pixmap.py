import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QLabel)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout(self)
        pixsel = QPixmap('DotA2.jpg')

        lbl = QLabel(self)
        lbl.setPixmap(pixsel)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(400, 400, 600, 300)
        self.setWindowTitle('Dota 2')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())