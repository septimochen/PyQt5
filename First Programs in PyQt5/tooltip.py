"""
ZetCode PyQt5 tutorial
This example shows a tooltip on
a window and a button.
"""
import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QToolTip, QWidget)
from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Source Code Pro', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Check', self)
        btn.setToolTip('This is a <b>PushButton</b> widget')
        btn.resize(btn.sizeHint())  # The sizeHint() method gives a recommended size for the button.
        btn.move(0, 1)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Dota 2')
        self.setWindowIcon(QIcon('dota_2.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
