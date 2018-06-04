import sys
from PyQt5.QtWidgets import QSlider, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setGeometry(200, 100, 300, 30)
        sld.setFocusPolicy(Qt.NoFocus)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 500, 500)




        self.setGeometry(500, 500, 640, 420)
        self.setWindowTitle('QSlider')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
