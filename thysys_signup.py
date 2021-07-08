# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thysys_signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(663, 486)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setGeometry(QtCore.QRect(260, 30, 161, 141))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("thyroid.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.thysysName = QtWidgets.QLabel(Form)
        self.thysysName.setGeometry(QtCore.QRect(290, 170, 111, 31))
        self.thysysName.setStyleSheet("color: rgb(255, 85, 127);\n"
"font: 87 14pt \"Arial Black\";\n"
"")
        self.thysysName.setObjectName("thysysName")
        self.username = QtWidgets.QTextEdit(Form)
        self.username.setGeometry(QtCore.QRect(190, 220, 291, 41))
        self.username.setStyleSheet("border: 4px solid rgb(85, 170, 255);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.username.setObjectName("username")
        self.password = QtWidgets.QTextEdit(Form)
        self.password.setGeometry(QtCore.QRect(190, 290, 291, 41))
        self.password.setStyleSheet("border: 4px solid rgb(85, 170, 255);\n"
"border-radius: 10px;")
        self.password.setObjectName("password")
        self.confirm_password = QtWidgets.QTextEdit(Form)
        self.confirm_password.setGeometry(QtCore.QRect(190, 360, 291, 41))
        self.confirm_password.setStyleSheet("border: 4px solid rgb(85, 170, 255);\n"
"border-radius: 10px;")
        self.confirm_password.setObjectName("confirm_password")
        self.usernameLabel = QtWidgets.QLabel(Form)
        self.usernameLabel.setGeometry(QtCore.QRect(160, 200, 81, 16))
        self.usernameLabel.setStyleSheet("color: rgb(190, 190, 190);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(160, 270, 91, 16))
        self.passwordLabel.setStyleSheet("color: rgb(190, 190, 190);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.passwordLabel.setObjectName("passwordLabel")
        self.confirmPasswordLabel = QtWidgets.QLabel(Form)
        self.confirmPasswordLabel.setGeometry(QtCore.QRect(160, 340, 151, 16))
        self.confirmPasswordLabel.setStyleSheet("color: rgb(190, 190, 190);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.Signup = QtWidgets.QPushButton(Form)
        self.Signup.setGeometry(QtCore.QRect(290, 420, 91, 31))
        self.Signup.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Arial\";\n"
"border-radius: 10px;")
        self.Signup.setObjectName("Signup")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 460, 161, 16))
        self.label.setStyleSheet("color: rgb(156, 156, 156);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 450, 93, 28))
        self.pushButton.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.thysysName.setText(_translate("Form", "THY-SYS"))
        self.usernameLabel.setText(_translate("Form", "Username"))
        self.passwordLabel.setText(_translate("Form", "Password"))
        self.confirmPasswordLabel.setText(_translate("Form", "Confirm Password"))
        self.Signup.setText(_translate("Form", "Sign Up"))
        self.label.setText(_translate("Form", "Already have an account?"))
        self.pushButton.setText(_translate("Form", "Log In Now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
