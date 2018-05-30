import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QLCDNumber, QSlider)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(400, 400, 250, 150)
        self.setWindowTitle('Signals and Slot')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


