import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Landing(QDialog):
    def __init__(self):
        super(Landing,self).__init__()
        loadUi("thysys_landing_page.ui",self)
        self.Login.clicked.connect(self.gotologin)
        self.Signup.clicked.connect(self.gotosignup)

    def gotologin(self):
        loginVar=Login()
        widget.addWidget(loginVar)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignup(self):
        signupVar = Signup()
        widget.addWidget(signupVar)
        widget.setCurrentIndex(widget.currentIndex()+1)



class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("thysys_login.ui",self)
        self.Login.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAcc.clicked.connect(self.gotosignup)

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        print("Successfully logged in with username ",username,"and password ", password)
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignup(self):
        signupVar=Signup()
        widget.addWidget(signupVar)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QDialog):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("thysys_signup.ui",self)
        self.Signup.clicked.connect(self.signupfunction)
        self.loginAcc.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def signupfunction(self):
        username = self.username.text()
        if self.password.text()==self.confirm_password.text():
            password = self.password.text()
            print("successfully created username",username,"with password",password)

    def gotologin(self):
        loginVar = Login()
        widget.addWidget(loginVar)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Homepage(QDialog):
    def __init__(self):
        super(Homepage,self).__init__()
        loadUi("thysys_homepage.ui",self)
        self.Logout.clicked.connect(self.gotoLanding)
        self.TakeAssessment.clicked.connect(self.gotoAssessment)
        self.MyResults.clicked.connect(self.gotoResult)

    def gotoLanding(self):
        landingVar = Landing()
        widget.addWidget(landingVar)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoAssessment(self):
        assessmentVar = Assessment()
        widget.addWidget(assessmentVar)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoResult(self):
        resultVar = Result()
        widget.addWidget(resultVar)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Assessment(QDialog):
    def __init__(self):
        super(Assessment,self).__init__()
        loadUi("thysys_assessmentPage.ui",self)
        self.Back.clicked.connect(self.gotoHome)
    
    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Result(QDialog):
    def __init__(self):
        super(Result,self).__init__()
        loadUi("thysys_results.ui",self)
        self.Back.clicked.connect(self.gotoHome)
        
    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

app=QApplication(sys.argv)
mainwindow=Landing()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(663)
widget.setFixedHeight(486)
widget.show()
app.exec_() 