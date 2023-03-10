# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#EAEEEF;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #4F6C77;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stats = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stats.setFont(font)
        self.stats.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.stats.setObjectName("stats")
        self.verticalLayout.addWidget(self.stats)
        self.db_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.db_button.setFont(font)
        self.db_button.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.db_button.setObjectName("db_button")
        self.verticalLayout.addWidget(self.db_button)
        self.terms_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.terms_button.setFont(font)
        self.terms_button.setStyleSheet("background-color: #A7C4D4;\n"
"color:#F6E8DA;")
        self.terms_button.setObjectName("terms_button")
        self.verticalLayout.addWidget(self.terms_button)
        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.test_button.setFont(font)
        self.test_button.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.test_button.setObjectName("test_button")
        self.verticalLayout.addWidget(self.test_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">????????????????</span></p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">????????????????</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">????????????????</span></p></body></html>"))
        self.stats.setText(_translate("MainWindow", "????????????????????"))
        self.db_button.setText(_translate("MainWindow", "???????????????????? ?? ???????????????? ????????????????"))
        self.terms_button.setText(_translate("MainWindow", "????????????????"))
        self.test_button.setText(_translate("MainWindow", "?????????? ???? ????????????????????????"))
