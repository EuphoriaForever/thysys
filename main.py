import sys
import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication


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

        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()

        c.execute('SELECT 1 FROM accounts WHERE account_name = ? AND password = ?', (username, password))
        conn.commit()  # conn.comit() will make it so that the SQL statement will be executed

        if len(c.fetchone()) == 1:
            print("Successfully logged in with username ", username, "and password ", password)
            homepageVar = Homepage()
            widget.addWidget(homepageVar)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            print("Account has yet to exist. will now hand u over to sign up page")
            self.gotosignup()

        # close our connection
        conn.close()

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
        if self.password.text() == self.confirm_password.text():
            password = self.password.text()

            # if password and confirm password are the same, we open a connection to database
            conn = sqlite3.connect("thysys.db")
            c = conn.cursor()
            # check if there exists an account with the same username we want
            c.execute('SELECT 1 FROM accounts WHERE account_name = ?', (username,))
            conn.commit() # conn.comit() will make it so that the SQL statement will be executed

            if len(c.fetchall()) > 0:
                print("Try another username")
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

    def gotoLanding(self):
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


class Assessment(QDialog):
    def __init__(self):
        super(Assessment, self).__init__()
        uic.loadUi("thysys_assessmentPage.ui", self)
        self.Back.clicked.connect(self.gotoHome)

    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        uic.loadUi("thysys_results.ui", self)
        self.Back.clicked.connect(self.gotoHome)

    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Landing()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(663)
widget.setFixedHeight(486)
widget.show()
app.exec_()
