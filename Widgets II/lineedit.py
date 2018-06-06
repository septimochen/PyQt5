import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        self.lbl.move(100, 50)

        self.le = QLineEdit(self)
        self.le.move(100, 110)
        self.le.textChanged[str].connect(self.onChanged)

        self.setGeometry(400, 400, 400, 300)
        self.setWindowTitle('Line Edit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
