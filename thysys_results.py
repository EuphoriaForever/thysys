# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thysys_results.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 600)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Back = QtWidgets.QPushButton(Form)
        self.Back.setGeometry(QtCore.QRect(20, 30, 61, 51))
        self.Back.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);\n"
"border-radius:20px;")
        self.Back.setObjectName("Back")
        self.thysysName = QtWidgets.QLabel(Form)
        self.thysysName.setGeometry(QtCore.QRect(350, 100, 111, 31))
        self.thysysName.setStyleSheet("color: rgb(255, 85, 127);\n"
"font: 87 14pt \"Arial Black\";\n"
"")
        self.thysysName.setObjectName("thysysName")
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setGeometry(QtCore.QRect(350, 10, 111, 91))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("thyroid.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 150, 801, 401))
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(135, 135, 135);\n"
"font-family: arial;\n"
"font-weight: bold;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(19)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 570, 291, 16))
        self.label_3.setStyleSheet("color: rgb(188, 188, 188);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Back.setText(_translate("Form", "Back"))
        self.thysysName.setText(_translate("Form", "THY-SYS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Prediction"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Age"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Pregnant"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Trimester"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Menstrual Cycle"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Goitre"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Smoking"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Family History"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Constipation"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Diarrhea"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Amount of Sleep"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Nervousness"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "Tiredness"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Hairloss"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Skin"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "Heart Rate"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Form", "Temperature"))
        self.label_3.setText(_translate("Form", "?? Icon from flaticon.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
