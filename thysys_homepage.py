# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thysys_homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 601)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MyResults = QtWidgets.QPushButton(Form)
        self.MyResults.setGeometry(QtCore.QRect(310, 350, 211, 61))
        self.MyResults.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";\n"
"border-radius: 15px;")
        self.MyResults.setObjectName("MyResults")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 20, 191, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("thyroid.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.TakeAssessment = QtWidgets.QPushButton(Form)
        self.TakeAssessment.setGeometry(QtCore.QRect(310, 260, 211, 61))
        self.TakeAssessment.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";\n"
"border-radius: 15px;")
        self.TakeAssessment.setObjectName("TakeAssessment")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 180, 141, 31))
        self.label_2.setStyleSheet("color: rgb(255, 85, 127);\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.Logout = QtWidgets.QPushButton(Form)
        self.Logout.setGeometry(QtCore.QRect(310, 450, 211, 61))
        self.Logout.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";\n"
"border-radius: 15px;")
        self.Logout.setObjectName("Logout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 580, 291, 16))
        self.label_3.setStyleSheet("color: rgb(188, 188, 188);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MyResults.setText(_translate("Form", "My Results"))
        self.TakeAssessment.setText(_translate("Form", "Take a self-assessment"))
        self.label_2.setText(_translate("Form", "THY-SYS"))
        self.Logout.setText(_translate("Form", "Log Out"))
        self.label_3.setText(_translate("Form", "?? Icon from flaticon.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
