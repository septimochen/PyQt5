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
        sld.setGeometry(100, 80, 200, 30)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.pixel1 = QPixmap('mute.png')
        self.pixel2 = QPixmap('min.png')
        self.pixel3 = QPixmap('med.png')
        self.pixel4 = QPixmap('max.png')

        self.label.setPixmap(self.pixel1.scaled(35, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        self.label.setGeometry(40, 75, 40, 40)


        self.setGeometry(500, 500, 340, 200)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(self.pixel1.scaled(35, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        elif 0 < value <= 30:
            self.label.setPixmap(self.pixel2.scaled(35, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        elif 30 < value <= 70:
            self.label.setPixmap(self.pixel3.scaled(35, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
        else:
            self.label.setPixmap(self.pixel4.scaled(35, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
