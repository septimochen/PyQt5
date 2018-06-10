from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(400, 400, 320, 240)
        self.setWindowTitle('Drawing points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, pt):
        pt.setPen(Qt.red)
        size = self.size()

        for i in range(400):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            pt.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
