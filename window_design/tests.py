# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tests.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 450)
        Form.setMinimumSize(QtCore.QSize(640, 450))
        Form.setMaximumSize(QtCore.QSize(1280, 900))
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form.setFont(font)
        Form.setStyleSheet("background-color:#EAEEEF;\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.trd_ans = QtWidgets.QRadioButton(Form)
        self.trd_ans.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.trd_ans.setObjectName("trd_ans")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.trd_ans)
        self.gridLayout.addWidget(self.trd_ans, 8, 0, 1, 3)
        self.s_ans = QtWidgets.QRadioButton(Form)
        self.s_ans.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.s_ans.setObjectName("s_ans")
        self.buttonGroup.addButton(self.s_ans)
        self.gridLayout.addWidget(self.s_ans, 7, 0, 1, 3)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color:#4F6C77;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#4F6C77;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.back = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.back.setObjectName("back")
        self.gridLayout.addWidget(self.back, 3, 2, 1, 1)
        self.f_ans = QtWidgets.QRadioButton(Form)
        self.f_ans.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.f_ans.setObjectName("f_ans")
        self.buttonGroup.addButton(self.f_ans)
        self.gridLayout.addWidget(self.f_ans, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#4F6C77;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 1)
        self.frth_ans = QtWidgets.QRadioButton(Form)
        self.frth_ans.setStyleSheet("background-color: #A7C4D4;\n"
"color: #F6E8DA;")
        self.frth_ans.setObjectName("frth_ans")
        self.buttonGroup.addButton(self.frth_ans)
        self.gridLayout.addWidget(self.frth_ans, 9, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#4F6C77;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Тест"))
        self.trd_ans.setText(_translate("Form", "ответ"))
        self.s_ans.setText(_translate("Form", "ответ"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Form", "ОПРЕДЕЛЕНИЕ:"))
        self.back.setText(_translate("Form", "НАЗАД"))
        self.f_ans.setText(_translate("Form", "ответ"))
        self.label.setText(_translate("Form", "Выбирите правильный ответ:"))
        self.pushButton.setText(_translate("Form", "Далее"))
        self.frth_ans.setText(_translate("Form", "ответ"))
        self.label_4.setText(_translate("Form", "Верно"))
