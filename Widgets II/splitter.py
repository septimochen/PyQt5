import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSplitter,
                             QHBoxLayout, QFrame, QStyleFactory)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        btm = QFrame(self)
        btm.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(btm)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.setGeometry(1024, 400, 300, 400)
        self.setWindowTitle("Splitter")
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())