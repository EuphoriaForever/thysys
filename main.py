import sys
import sqlite3
from typing import Union, Any

from chefboost import Chefboost as cb
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtGui import QDoubleValidator, QValidator
from PyQt5.QtWidgets import QMessageBox
from joblib import dump, load
import sklearn
import mlxtend
# provides common algorithm like decision trees, neural networks, etc
from sklearn.svm import SVC, NuSVC
from mlxtend.classifier import StackingClassifier, StackingCVClassifier

uName = ""
uResult = ""
uResultID = {}
uDetail = ""
uText = ""


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
        global uResultID
        uResultID = {}
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
        msg.setInformativeText(
            "THY-SYS is an app that helps predict the likelihood of a person experiencing thyroid diseases based on their symptoms")
        msg.setDetailedText(
            "To predict what you may be experiencing, click the TAKE A SELF-ASSESSMENT button. To see results from previous assessment, click the RESULT button")
        x = msg.exec_()


class Assessment(QDialog):
    def __init__(self):
        super(Assessment, self).__init__()
        uic.loadUi("thysys_assessmentPage.ui", self)
        self.Back.clicked.connect(self.gotoHome)
        # Commented out for testing purposes
        # self.submitButton.clicked.connect(self.goResult)
        self.submitButton.clicked.connect(self.goRecodeResponse)
        print("Your name is ", uName)

    def gotoHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoError(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def checkAssessmentResponse(self):
        isNotEmpty = self.ageInput.text() != ""
        isMF = self.MalecheckBox.isChecked() or self.FemalecheckBox.isChecked()
        isPregnant = self.YesPregnant.isChecked() or self.NoPregnant.isChecked()
        whatTrimester = self.FirstTri.isChecked() or self.SecondTri.isChecked() or self.ThirdTri.isChecked() or self.NATri.isChecked()
        isBleeding = self.NormalMens.isChecked() or self.AbMens.isChecked() or self.NAMens.isChecked()
        isSwelling = self.YesSwelling.isChecked() or self.NoSwelling.isChecked()
        isSmoker = self.YesSmoke.isChecked() or self.NoSmoke.isChecked()
        noHistory = self.YesHistory.isChecked() or self.NoHistory.isChecked()
        isConst = self.YesEmpty.isChecked() or self.NoEmpty.isChecked()
        isLoose = self.YesLoose.isChecked() or self.NoLoose.isChecked()
        isSleep = self.LessSleep.isChecked() or self.MoreSleep.isChecked() or self.NormalSleep.isChecked()
        isUneasy = self.YesUneasy.isChecked() or self.NoUneasy.isChecked()
        isTired = self.YesTired.isChecked() or self.NoTired.isChecked()
        isHairloss = self.YesHairLoss.isChecked() or self.NoHairLoss.isChecked()
        weightChange = self.GainWeight.isChecked() or self.LossWeight.isChecked() or self.NormalWeight.isChecked()
        skinChange = self.AbnormalSkin.isChecked() or self.NormalSkin.isChecked()
        heartRateChange = self.LowHeart.isChecked() or self.HighHeart.isChecked() or self.NormalHeight.isChecked()
        tempChange = self.LowTemp.isChecked() or self.NormalTemp.isChecked() or self.HighTemp.isChecked()

        if isNotEmpty and isMF and isSwelling and isSmoker and noHistory \
                and isConst and isLoose and isSleep and isUneasy and isTired and isHairloss and weightChange and skinChange \
                and heartRateChange and tempChange:
            if self.MalecheckBox.isChecked():  # since we confirmed nga nacheck ang gender, we check WHAT gender
                return True
            elif self.FemalecheckBox.isChecked():
                if isPregnant and whatTrimester and isBleeding:
                    return True
                else:
                    return False
        else:
            return False

    def goRecodeResponse(self):
        if self.checkAssessmentResponse():  # checks if the form is incomplete or empty

            # Checks if the input in the textbox is a number from 1 to 150
            validation_rule = QDoubleValidator(1, 150, 0)
            if validation_rule.validate(self.ageInput.text(), 1)[0] == QValidator.Acceptable:
                age = int(self.ageInput.text())
            else:
                self.gotoError("Invalid Age")

            # Checks to see if the examinee is Male or Female
            if self.MalecheckBox.isChecked():
                gender_chaid = "M"
                gender_stack = 0
            else:
                gender_chaid = "F"
                gender_stack = 1

            # If Male, set prengancy, trimester, and menstrual bleeding to Not Applicable by default
            if gender_stack == 0:
                pregnant_chaid = trimester_chaid = mens_chaid = "NaN"
                pregnant_stack = mens_stack = 2
                trimester_stack = 3
            else:
                # Pregnancy
                if self.YesPregnant.isChecked():
                    pregnant_chaid = "YES"
                    pregnant_stack = 1
                else:
                    pregnant_chaid = "NO"
                    pregnant_stack = 0

                # Trimester
                if self.FirstTri.isChecked():
                    trimester_chaid = "1ST"
                    trimester_stack = 0
                elif self.SecondTri.isChecked():
                    trimester_chaid = "2ND"
                    trimester_stack = 1
                elif self.SecondTri.isChecked():
                    trimester_chaid = "3RD"
                    trimester_stack = 2
                else:
                    trimester_chaid = "NaN"
                    trimester_stack = 3

                # Menstrual Bleeding
                if self.NormalMens.isChecked():
                    mens_chaid = "NORMAL"
                    mens_stack = 1
                else:
                    mens_chaid = "ABNORMAL"
                    mens_stack = 0

            # Everything else that has nothing to do with se is recoded
            # Goitre
            if self.YesSwelling.isChecked():
                goitre_chaid = "YES"
                goitre_stack = 1
            else:
                goitre_chaid = "NO"
                goitre_stack = 0

            # Smoker
            if self.YesSmoke.isChecked():
                smoke_chaid = "YES"
                smoke_stack = 1
            else:
                smoke_chaid = "NO"
                smoke_stack = 0

            # Family History
            if self.YesHistory.isChecked():
                family_chaid = "YES"
                family_stack = 1
            else:
                family_chaid = "NO"
                family_stack = 0

            # Constipation
            if self.YesEmpty.isChecked():
                constipation_chaid = "YES"
                constipation_stack = 1
            else:
                constipation_chaid = "NO"
                constipation_stack = 0

            # Diarrhoea
            if self.YesLoose.isChecked():
                diarrhea_chaid = "YES"
                diarrhea_stack = 1
            else:
                diarrhea_chaid = "NO"
                diarrhea_stack = 0

            # Sleepiness
            if self.LessSleep.isChecked():
                sleepiness_chaid = "LESS"
                sleepiness_stack = 0
            elif self.MoreSleep.isChecked():
                sleepiness_chaid = "MORE"
                sleepiness_stack = 2
            else:
                sleepiness_chaid = "NORMAL"
                sleepiness_stack = 1

            # Nervousness
            if self.YesUneasy.isChecked():
                nervous_chaid = "YES"
                nervous_stack = 1
            else:
                nervous_chaid = "NO"
                nervous_stack = 0

            # Feeling Tired
            if self.YesTired.isChecked():
                tired_chaid = "YES"
                tired_stack = 1
            else:
                tired_chaid = "NO"
                tired_stack = 0

            # Hair loss
            if self.YesHairLoss.isChecked():
                hairloss_chaid = "YES"
                hairloss_stack = 1
            else:
                hairloss_chaid = "NO"
                hairloss_stack = 0

            # Weight
            if self.GainWeight.isChecked():
                weight_chaid = "GAIN"
                weight_stack = 2
            elif self.LossWeight.isChecked():
                weight_chaid = "LOSS"
                weight_stack = 0
            else:
                weight_chaid = "NORMAL"
                weight_stack = 1

            # Skin
            if self.AbnormalSkin.isChecked():
                skin_chaid = "ABNORMAL"
                skin_stack = 0
            else:
                skin_chaid = "NORMAL"
                skin_stack = 1

            # Heart Rate
            if self.LowHeart.isChecked():
                heart_chaid = "LOW"
                heart_stack = 0
            elif self.HighHeart.isChecked():
                heart_chaid = "HIGH"
                heart_stack = 2
            else:
                heart_chaid = "NORMAL"
                heart_stack = 1

            # Body Temperature
            if self.LowTemp.isChecked():
                temp_chaid = "LOW"
                temp_stack = 0
            elif self.HighTemp.isChecked():
                temp_chaid = "HIGH"
                temp_stack = 2
            else:
                temp_chaid = "NORMAL"
                temp_stack = 1

            # Chaid and Stack Values
            values_chaid = [age, gender_chaid, pregnant_chaid, trimester_chaid, goitre_chaid, smoke_chaid,
                            hairloss_chaid, constipation_chaid, diarrhea_chaid, family_chaid, nervous_chaid,
                            skin_chaid, mens_chaid, tired_chaid, sleepiness_chaid, weight_chaid,
                            heart_chaid, temp_chaid]
            values_stack = [age, gender_stack, pregnant_stack, trimester_stack, goitre_stack, smoke_stack,
                            hairloss_stack, constipation_stack, diarrhea_stack, family_stack, nervous_stack,
                            skin_stack, mens_stack, tired_stack, sleepiness_stack, weight_stack,
                            heart_stack, temp_stack]
            self.gotoStackResult(values_stack, values_chaid)
        else:
            self.gotoError("Incomplete Form.")

    def saveToDatabase(self, values, results):
        # saving to database
        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()
        c.execute("INSERT INTO results(username, age, gender, pregnant, trimester, goitre, smoke, hairloss, "
                  "constipation, diarrhea, family, nervous, skin, menstrual, tired, sleepiness, weight, "
                  "heart, temp, class, created_at) "
                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,datetime('now','localtime'))", (
                      uName, values[0], values[1], values[2], values[3], values[4], values[5], values[6],
                      values[7], values[8], values[9], values[10], values[11], values[12], values[13],
                      values[14], values[15], values[16], values[17], results))
        conn.commit()
        conn.close()
        resultV = Result()
        widget.addWidget(resultV)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def interpretClass(self, prediction):
        if prediction == 0:
            return "Hypothyroidism"
        elif prediction == 1:
            return "Euthyroidism"
        else:
            return "Hyperthyroidism"

    def gotoStackResult(self, values_stack, values_chaid):
        svm_knn = load('svm-knn-7.joblib')
        resultsPredict = svm_knn.predict([values_stack])
        resultsPredict = self.interpretClass(resultsPredict[0])
        print("The application predicts that you may be experiencing ", resultsPredict)
        global uResult
        uResult = resultsPredict

        # Call method to save to database
        self.saveToDatabase(values_chaid, resultsPredict)
        # after saving, we go to the one time result page
        self.goToOneTime()

    def goToOneTime(self):
        oneVar = OneTimeResult()
        widget.addWidget(oneVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class OneTimeResult(QDialog):
    def __init__(self):
        super(OneTimeResult, self).__init__()
        uic.loadUi("thysys_one_result.ui", self)
        self.Back.clicked.connect(self.backToHome)
        self.myResults.clicked.connect(self.goToResultsList)
        self.loadPage()

    def backToHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        global uResult
        uResult = ""

    def loadPage(self):
        global uResult
        if uResult == 'Euthyroidism':
            uResult = "  Normal Thyroid"

        self.results.setText(uResult)

    def goToResultsList(self):
        resultVar = Result()
        widget.addWidget(resultVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        global uResult
        uResult = ""


class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        uic.loadUi("thysys_results.ui", self)
        self.Back.clicked.connect(self.goHome)
        self.loadData()

    def loadData(self):
        global uResultID
        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()

        self.tableWidget.setRowCount(0)
        rowCount = self.tableWidget.rowCount()
        tableIndex = 0
        for row in c.execute('SELECT * FROM results WHERE username = ?', (uName,)):
            self.tableWidget.setRowCount(rowCount + 1)
            self.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(row[21]))
            self.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(row[20]))
            uResultID[tableIndex] = row[0]
            buttoning = QPushButton('View Details', self)
            buttoning.clicked.connect(lambda ch, i=uResultID[tableIndex]: self.goToDetails(i))
            self.tableWidget.setCellWidget(tableIndex, 2, buttoning)
            print(row)
            tableIndex += 1
            rowCount += 1
        print(uResultID)

    def goHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        global uResultID
        uResultID = {}

    def goToDetails(self, numVar):
        print('aye ', numVar)
        global uDetail
        uDetail = numVar
        detailVar = Details()
        widget.addWidget(detailVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Details(QDialog):
    def __init__(self):
        super(Details, self).__init__()
        uic.loadUi("thysys_details.ui", self)
        self.Back.clicked.connect(self.goBackToResults)
        self.Home.clicked.connect(self.goBackHome)
        self.SaveTextFile.clicked.connect(self.SaveText)
        self.loadTheData()

    def loadTheData(self):
        global uText
        conn = sqlite3.connect("thysys.db")
        c = conn.cursor()
        for row in c.execute('SELECT * FROM results WHERE result_id = ?', (uDetail,)):
            self.Predict.setText(row[20])
            self.Age.setText(row[2])
            self.Gender.setText(row[3])
            if row[3] == 'F':
                self.PregnantLabel.setText('Pregnant:')
                self.Pregnant.setText(row[4])
                self.TrimesterLabel.setText('Trimester:')
                self.Trimester.setText(row[5])
                self.MenstrualLabel.setText('Menstrual Cycle:')
                self.Menstrual.setText(row[14])
            self.Goitre.setText(row[6])
            self.Smoking.setText(row[7])
            self.Family.setText(row[11])
            self.Constipation.setText(row[9])
            self.Diarrhea.setText(row[10])
            self.Tired.setText(row[15])
            self.Nervous.setText(row[12])
            self.Sleep.setText(row[16])
            self.Hairloss.setText(row[8])
            self.Skin.setText(row[13])
            self.Weight.setText(row[17])
            self.HeartRate.setText(row[18])
            self.Temperature.setText(row[19])

            if row[3] == 'M':
                uText = ["Date:", row[21], "\nPrediction:", row[20], "\nAge:", row[2], "\nGender:", row[3], "\nGoitre:",
                         row[6], "\nSmoking:", row[7], "\nHistory of thyroid disease in the family:", row[11],
                         "\nConstipation:", row[9], "\nDiarrhea:", row[10], "\nTired:", row[15], "\nNervous:", row[12],
                         "\nSleep:", row[16], "\nHairloss:", row[8], "\nSkin:", row[13], "\nWeight:", row[17],
                         "\nHeart Rate:", row[18], "\nTemperature:", row[19]]
            else:
                uText = ["Date:", row[21], "\nPrediction:", row[20], "\nAge:", row[2], "\nGender:", row[3],
                         "\nPregnant:", row[4], "\nTrimester:", row[5], "\nMenstrual Cycle:", row[14], "\nGoitre:", row[6], "\nSmoking:",
                         row[7], "\nHistory of thyroid disease in the family:", row[11],"\nConstipation:", row[9], "\nDiarrhea:",
                         row[10], "\nTired:", row[15], "\nNervous:", row[12], "\nSleep:", row[16], "\nHairloss:", row[8],
                         "\nSkin:", row[13], "\nWeight:", row[17], "\nHeart Rate:", row[18], "\nTemperature:", row[19]]

    def goBackToResults(self):
        resultVar = Result()
        widget.addWidget(resultVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        global uDetail
        uDetail = ""

    def goBackHome(self):
        homepageVar = Homepage()
        widget.addWidget(homepageVar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        global uDetail
        uDetail = ""

    def SaveText(self):
        global uDetail
        uDetail = 'MyResults'+str(uDetail)
        filename = "%s.txt" % uDetail
        file1 = open(filename, "w")
        file1.writelines(uText)
        file1.close()  # to change file access modes


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
