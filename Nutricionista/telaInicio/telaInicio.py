# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 904)
        MainWindow.setStyleSheet("font: \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(176, 160, 255, 255), stop:1 rgba(165, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 290, 161, 161))
        self.label.setStyleSheet("background-color: none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/Pufferfish_29_JE4_BE1.webp"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_cadastroPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastroPaciente.setGeometry(QtCore.QRect(300, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_cadastroPaciente.setFont(font)
        self.pushButton_cadastroPaciente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastroPaciente.setStyleSheet("background-color: none;")
        self.pushButton_cadastroPaciente.setObjectName("pushButton_cadastroPaciente")
        self.pushButton_controlDiteta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_controlDiteta.setGeometry(QtCore.QRect(480, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_controlDiteta.setFont(font)
        self.pushButton_controlDiteta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_controlDiteta.setStyleSheet("background-color: none;")
        self.pushButton_controlDiteta.setObjectName("pushButton_controlDiteta")
        self.pushButton_registroPaciente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_registroPaciente.setGeometry(QtCore.QRect(670, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_registroPaciente.setFont(font)
        self.pushButton_registroPaciente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_registroPaciente.setStyleSheet("background-color: none;")
        self.pushButton_registroPaciente.setObjectName("pushButton_registroPaciente")
        self.pushButton_agenda = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_agenda.setGeometry(QtCore.QRect(850, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_agenda.setFont(font)
        self.pushButton_agenda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_agenda.setStyleSheet("background-color: none;")
        self.pushButton_agenda.setObjectName("pushButton_agenda")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 300, 511, 401))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 470, 431, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 21))
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
        self.label_2.setText(_translate("MainWindow", "PufferFish Nutricionista"))
        self.pushButton_cadastroPaciente.setText(_translate("MainWindow", "Cadastar Paciente"))
        self.pushButton_controlDiteta.setText(_translate("MainWindow", "Controle de dieta"))
        self.pushButton_registroPaciente.setText(_translate("MainWindow", "Registros de Paciente"))
        self.pushButton_agenda.setText(_translate("MainWindow", "Agenda"))
        self.label_3.setText(_translate("MainWindow", "TextLabelLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))
        self.label_4.setText(_translate("MainWindow", "Temos os doutores mais capacitados do mercado contando com a presença ilustre do Doutor Baiacu do Mine"))
