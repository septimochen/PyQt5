import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Ubuntu", self)
        self.lbl.setGeometry(200, 150, 100, 100)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Fedora")
        combo.addItem("RedHatsss")
        combo.addItem("MacOs X")

        combo.move(50, 50)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(400, 400, 400, 300)
        self.setWindowTitle("Combo Box")
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.adjustSize()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
