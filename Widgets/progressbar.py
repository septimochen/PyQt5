import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QProgressBar)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pb = QProgressBar(self)
        self.pb.setGeometry(100, 40, 250, 32)

        self.btn = QPushButton('Start', self)
        self.btn.move(160, 90)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(400, 300, 400, 200)
        self.setWindowTitle("Progress Bar")
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.btn.setText('Finished')
            return
        self.step += 1
        self.pb.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
