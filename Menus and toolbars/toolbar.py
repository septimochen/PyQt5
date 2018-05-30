import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tool bar')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())