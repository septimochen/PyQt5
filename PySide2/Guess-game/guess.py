from PySide2 import QtCore, QtGui, QtWidgets
import sys
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(304, 282)
        self.number = random.randint(0, 300)
        self.count = 0

        self.guessButton = QtWidgets.QPushButton(Form)
        self.guessButton.setGeometry(QtCore.QRect(110, 120, 75, 23))
        self.guessButton.setObjectName("pushButton")
        self.guessButton.clicked.connect(self.guess)

        self.text = QtWidgets.QLineEdit(Form)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(QtCore.QRect(70, 60, 171, 41))
        self.text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.text.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 150, 151, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 190, 71, 31))
        self.lcdNumber.display(self.count)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(93, 190, 61, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.guessButton.setText(QtWidgets.QApplication.translate("Form", "Guess", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Please give a try!</span></p></body></html>", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Attempts:</span></p></body></html>", None, -1))

    def guess(self):
        self.temp = int(self.text.text())
        print(self.number)
        self.count+=1

        if self.temp > self.number:
            self.label.setText("Too Big!")
            self.text.setFocus()

        elif self.temp < self.number:
            self.label.setText("Too Small!")
            self.text.setFocus()

        else:
            self.label.setText("Bingo!!!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
