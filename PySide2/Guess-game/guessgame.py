from PySide2 import QtWidgets, QtCore, QtGui
import sys


class GuessGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        l_edit = QtWidgets.QLineEdit()
        confirm_button = QtWidgets.QPushButton("Guess")
        text = QtWidgets.QLabel("Please give a try! ")
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(l_edit)
        layout.addWidget(text)
        layout.addWidget(confirm_button)

        self.setLayout(layout)
        self.setWindowTitle("Guess Game")
        self.resize(600, 400)
        self.show()


app = QtWidgets.QApplication(sys.argv)
game = GuessGame()
sys.exit(app.exec_())

