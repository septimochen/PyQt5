"""
ZetCode PyQt5 tutorial

This program shows a confirmation
message box when we click on the close
button of the application window.

"""
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Message Box")
        self.show()

    # If we close a QWidget, the QCloseEvent is generated.
    # To modify the widget behaviour we need to re-implement the closeEvent() event handler.

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?', QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # We show a message box with two buttons: Yes and No.
    # The first string appears on the title bar. The second string is the message text displayed by the dialog.
    # The third argument specifies the combination of buttons appearing in the dialog.
    # The last parameter is the default button. It is the button which has initially the keyboard focus. T
    # he return value is stored in the reply variable.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
