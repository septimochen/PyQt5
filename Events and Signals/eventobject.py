import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(400, 400, 440, 330)
        self.setWindowTitle('Event Object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text2 = "x: {0}___________ y: {1}".format(x, y)
        self.label.setText(text2)


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())