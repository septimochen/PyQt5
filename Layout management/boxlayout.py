import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout,
                             QVBoxLayout, QWidget, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okbtn = QPushButton('Ok')
        cancelbtn = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(440, 330, 600, 440)
        self.setWindowTitle("Box Layout")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
