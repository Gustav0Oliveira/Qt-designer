# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reprodutor musicarl.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parar = QtWidgets.QPushButton(self.centralwidget)
        self.parar.setGeometry(QtCore.QRect(470, 370, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.parar.setFont(font)
        self.parar.setObjectName("parar")
        self.tocar = QtWidgets.QPushButton(self.centralwidget)
        self.tocar.setGeometry(QtCore.QRect(470, 170, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tocar.setFont(font)
        self.tocar.setObjectName("tocar")
        self.pausar = QtWidgets.QPushButton(self.centralwidget)
        self.pausar.setGeometry(QtCore.QRect(470, 590, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pausar.setFont(font)
        self.pausar.setObjectName("pausar")
        self.verticalSlider_volume = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_volume.setGeometry(QtCore.QRect(890, 360, 22, 160))
        self.verticalSlider_volume.setMaximum(100)
        self.verticalSlider_volume.setSliderPosition(50)
        self.verticalSlider_volume.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_volume.setObjectName("verticalSlider_volume")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 290, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parar.setText(_translate("MainWindow", "Parar"))
        self.tocar.setText(_translate("MainWindow", "Tocar"))
        self.pausar.setText(_translate("MainWindow", "Pausar"))
        self.label.setText(_translate("MainWindow", "Volume"))
