import pandas as pd
from PySide2 import QtCore, QtGui, QtWidgets
import sys


df = pd.read_csv("data/estatetop100.csv")


# print(df.loc[df.name.isin(search("万科")), ('rank', 'name')])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 517)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QLabel(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 170, 581, 321))
        self.tableView.setObjectName("tableView")
        self.ls = []



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 70, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)

        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(80, 70, 271, 61))
        self.text.setObjectName("lineEdit")
        self.text.selectAll()
        self.text.setFocus()


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "搜索", None, -1))

    def search(self):
        self.ls = []
        self.word = self.text.text()
        for company in list(df.name):
            if self.word in company:
                self.ls.append(company)

        # print(df.loc[df.name.isin(ls), ('rank', 'name')])
        self.tableView.setText(df.loc[df.name.isin(self.ls), ('rank', 'name')].set_index('rank').to_string())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())