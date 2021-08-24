import sys
import sqlite3
from typing import Union, Any

from chefboost import Chefboost as cb
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from joblib import dump, load
import sklearn
import mlxtend
#provides common algorithm like decision trees, neural networks, etc
from sklearn.svm import SVC, NuSVC
from mlxtend.classifier import StackingClassifier, StackingCVClassifier

uName = ""


class Landing(QDialog):
    def __init__(self):
        super(Landing, self).__init__()
        uic.loadUi("thysys_landing_page.ui", self)
        self.Login.clicked.connect(self.gotologin)
        self.Signup.clicked.connect(self.gotosignup)

    def gotologin(self):
        loginVar = Login()
        widget.addWidget(loginVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosignup(self):
        signupVar = Signup()
        widget.addWidget(signupVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("thysys_login.ui", self)
        self.Login.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAcc.clicked.connect(self.gotosignup)

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()

        if len(username) == 0 or len(password) == 0:
            self.error.setText("Please input a username or password")
        else:
            conn = sqlite3.connect("thysys.db")
            c = conn.cursor()

            query = 'SELECT password FROM accounts WHERE account_name=\'' + username + "\'"
            c.execute(query)
            resultPass = c.fetchone()  # conn.comit() will make it so that the SQL statement will be executed

            if resultPass is not None:
                if resultPass[0] == password:
                    print("Successfully logged in with username ", username, "and password ", password)
                    global uName
                    uName = username
                    homepageVar = Homepage()
                    widget.addWidget(homepageVar)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                    self.error.setText("")
                else:
                    self.error.setText('Invalid password')
            else:
                self.error.setText("Invalid username")
            # except Exception as e:
            #     self.error.setText("Invalid username")
            #     print('Exception: {}'.format(e))
            #     raise Exception(e)

    def gotosignup(self):
        signupVar = Signup()
        widget.addWidget(signupVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        uic.loadUi("thysys_signup.ui", self)
        self.Signup.clicked.connect(self.signupfunction)
        self.loginAcc.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def signupfunction(self):
        username = self.username.text()
        password = self.password.text()
        if len(username) == 0 or len(password) == 0:
            self.error.setText("Please input a username or password")
        else:
            if password == self.confirm_password.text():
                password = self.password.text()

                # if password and confirm password are the same, we open a connection to database
                conn = sqlite3.connect("thysys.db")
                c = conn.cursor()
                # check if there exists an account with the same username we want
                c.execute('SELECT 1 FROM accounts WHERE account_name = ?', (username,))
                conn.commit()  # conn.comit() will make it so that the SQL statement will be executed

                if len(c.fetchall()) > 0:
                    print("Try another username")
                    self.error.setText("Username already exists")
                else:
                    print("does not exist")
                    c.execute("INSERT INTO accounts(account_name,password,is_active,created_at,updated_at,is_admin) "
                              "VALUES (?,?,1,datetime('now','localtime'),NULL,1)", (username, password))
                    conn.commit()
                    print("successfully created username", username, "with password", password)
                    homepageVar = Homepage()
                    widget.addWidget(homepageVar)
                    widget.setCurrentIndex(widget.currentIndex() + 1)

                # close our connection
                conn.close()
            else:
                print("password and confirm password does not match. try again")
                self.error.setText("Passwords did not match")

    def gotologin(self):
        loginVar = Login()
        widget.addWidget(loginVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Homepage(QDialog):
    def __init__(self):
        super(Homepage, self).__init__()
        uic.loadUi("thysys_homepage.ui", self)
        self.Logout.clicked.connect(self.gotoLanding)
        self.TakeAssessment.clicked.connect(self.gotoAssessment)
        self.MyResults.clicked.connect(self.gotoResult)
        self.info.clicked.connect(self.popUpMessage)

    def gotoLanding(self):
        global uName
        uName = ""
        landingVar = Landing()
        widget.addWidget(landingVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoAssessment(self):
        assessmentVar = Assessment()
        widget.addWidget(assessmentVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoResult(self):
        resultVar = Result()
        widget.addWidget(resultVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def popUpMessage(self):
        msg = QMessageBox()
        msg.setWindowTitle("About THY-SYS")
        msg.setText("Hello and welcome to THY-SYS")
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText("THY-SYS is an app that helps predict the likelihood of a person experiencing thyroid diseases based on their symptoms")
        msg.setDetailedText("To predict what you may be experiencing, click the TAKE A SELF-ASSESSMENT button. To see results from previous assessment, click the RESULT button")
        x = msg.exec_()


class Assessment(QDialog):
    def __init__(self):
        super(Assessment, self).__init__()
        uic.loadUi("thysys_assessmentPage.ui", self)
        self.Back.clicked.connect(self.gotoHome)
        #Commented out for testing purposes
        # self.submitButton.clicked.connect(self.goResult)
        self.submitButton.clicked.connect(self.svm_knn_result)
        print("Your name is ", uName)
        print (mlxtend.__version__)

    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goResult(self):
        chaidModel = cb.load_model(file_name="chaidModel.pkl")

        age = self.ageInput.text()
        print(age)

        if self.MalecheckBox.isChecked():
            gender = "M"
        else:
            gender = "F"

        if self.YesPregnant.isChecked():
            pregnant = "YES"
        elif self.NoPregnant.isChecked():
            pregnant = "NO"
        else:
            pregnant = "NaN"

        if self.FirstTri.isChecked():
            trimester = "1ST"
        elif self.SecondTri.isChecked():
            trimester = "2ND"
        elif self.SecondTri.isChecked():
            trimester = "3RD"
        else:
            trimester = "NaN"

        if self.NormalMens.isChecked():
            menstrualBleeding = "NORMAL"
        elif self.AbMens.isChecked():
            menstrualBleeding = "ABNORMAL"
        else:
            menstrualBleeding = "NaN"

        if self.YesSwelling.isChecked():
            goitre = "YES"
        else:
            goitre = "NO"

        if self.YesSmoke.isChecked():
            smoke = "YES"
        else:
            smoke = "NO"

        if self.YesHistory.isChecked():
            family = "YES"
        else:
            family = "NO"

        if self.YesEmpty.isChecked():
            constipation = "YES"
        else:
            constipation = "NO"

        if self.YesLoose.isChecked():
            diarrhea = "YES"
        else:
            diarrhea = "NO"

        if self.LessSleep.isChecked():
            sleepiness = "LESS"
        elif self.MoreSleep.isChecked():
            sleepiness = "MORE"
        else:
            sleepiness = "NORMAL"

        if self.YesUneasy.isChecked():
            nervous = "YES"
        else:
            nervous = "NO"

        if self.YesTired.isChecked():
            tired = "YES"
        else:
            tired = "NO"

        if self.YesHairLoss.isChecked():
            hairloss = "YES"
        else:
            hairloss = "NO"

        if self.GainWeight.isChecked():
            weight = "GAIN"
        elif self.LossWeight.isChecked():
            weight = "LOSS"
        else:
            weight = "NORMAL"

        if self.AbnormalSkin.isChecked():
            skin = "ABNORMAL"
        else:
            skin = "NORMAL"

        if self.LowHeart.isChecked():
            heart = "LOW"
        elif self.HighHeart.isChecked():
            heart = "HIGH"
        else:
            heart = "NORMAL"

        if self.LowTemp.isChecked():
            temp = "LOW"
        elif self.HighTemp.isChecked():
            temp = "HIGH"
        else:
            temp = "NORMAL"

        values = [age, gender, pregnant, trimester, goitre, smoke, hairloss, constipation, diarrhea, family, nervous,
                  skin, menstrualBleeding, tired, sleepiness, weight, heart, temp]

        resultsPredict = cb.predict(chaidModel, values)

        print("The application predicts that you may be experiencing ", resultsPredict)
        print(uName)
        # saving to database
        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()
        c.execute("INSERT INTO results(username, age, gender, pregnant, trimester, goitre, smoke, hairloss, "
                  "constipation, diarrhea, family, nervous, skin, menstrual, tired, sleepiness, weight, "
                  "heart, temp, class, created_at) "
                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now','localtime'))", (
                      uName, age, gender, pregnant, trimester, goitre, smoke, hairloss, constipation, diarrhea, family,
                      nervous,
                      skin, menstrualBleeding, tired, sleepiness, weight, heart, temp, resultsPredict))
        conn.commit()
        conn.close()
        resultV = Result()
        widget.addWidget(resultV)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def svm_knn_result(self):
        print("YO")
        svm_knn = load('svm-knn-7.joblib')
        print(svm_knn.predict([[56,1,1,2,1,0,0,0,1,0,1,0,1,1,0,0,2,2]]))

class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        uic.loadUi("thysys_results.ui", self)
        self.Back.clicked.connect(self.goHome)
        self.loadData()

    def loadData(self):
        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()

        self.tableWidget.setRowCount(0)
        rowCount = self.tableWidget.rowCount()
        tableIndex = 0
        for row in c.execute('SELECT * FROM results WHERE username = ?', (uName,)):
            self.tableWidget.setRowCount(rowCount + 1)
            self.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(row[20]))
            self.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(row[14]))
            self.tableWidget.setItem(tableIndex, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tableIndex, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tableIndex, 8, QtWidgets.QTableWidgetItem(row[11]))
            self.tableWidget.setItem(tableIndex, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tableIndex, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tableIndex, 11, QtWidgets.QTableWidgetItem(row[16]))
            self.tableWidget.setItem(tableIndex, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.tableWidget.setItem(tableIndex, 13, QtWidgets.QTableWidgetItem(row[15]))
            self.tableWidget.setItem(tableIndex, 14, QtWidgets.QTableWidgetItem(row[8]))
            self.tableWidget.setItem(tableIndex, 15, QtWidgets.QTableWidgetItem(row[17]))
            self.tableWidget.setItem(tableIndex, 16, QtWidgets.QTableWidgetItem(row[13]))
            self.tableWidget.setItem(tableIndex, 17, QtWidgets.QTableWidgetItem(row[18]))
            self.tableWidget.setItem(tableIndex, 18, QtWidgets.QTableWidgetItem(row[19]))
            print(row)
            tableIndex += 1
            rowCount += 1

    def goHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Landing()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(801)
widget.setFixedHeight(601)
widget.setWindowTitle("THY-SYS")
widget.setWindowIcon(QtGui.QIcon('thyroid.png'))
widget.show()
app.exec_()
