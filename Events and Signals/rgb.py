# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgb.ui',
# licensing of 'rgb.ui' applies.
#
# Created: Tue Jun 26 21:46:10 2018
#      by: pyside2-uic  running on PySide2 5.11.0a1.dev1528474042
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 529)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(Form)
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_2.addWidget(self.verticalSlider_2, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 1, 0, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(Form)
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout_3.addWidget(self.verticalSlider_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL("valueChanged(int)"), self.spinBox.setValue)
        QtCore.QObject.connect(self.verticalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_2.setValue)
        QtCore.QObject.connect(self.verticalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.spinBox_3.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "RGB", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Red", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Green", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Blue", None, -1))

