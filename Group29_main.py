# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from datetime import datetime
import numpy as np
import cv2
import pickle
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 737)
        MainWindow.setMaximumSize(QtCore.QSize(1052, 715))
        font = QtGui.QFont()
        font.setPointSize(72)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(75, 75, 85);\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1052, 715))
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setEnabled(True)
        self.loginButton.setGeometry(QtCore.QRect(235, 182, 581, 361))
        self.loginButton.setMinimumSize(QtCore.QSize(581, 361))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.loginButton.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"alternate-background-color: rgb(41, 255, 38);\n"
"border: 4px solid rgb(124, 124, 134);\n"
"border-radius: 30px;\n"
"font: 40pt \"MS Shell Dlg 2\";")
        self.loginButton.setObjectName("loginButton")
        self.stackedWidget.addWidget(self.loginPage)
        self.cameraPage = QtWidgets.QWidget()
        self.cameraPage.setObjectName("cameraPage")
        self.camFeed = QtWidgets.QLabel(self.cameraPage)
        self.camFeed.setGeometry(QtCore.QRect(265, 80, 521, 381))
        self.camFeed.setMinimumSize(QtCore.QSize(521, 381))
        self.camFeed.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.camFeed.setText("")
        self.camFeed.setObjectName("camFeed")
        self.backButton = QtWidgets.QPushButton(self.cameraPage)
        self.backButton.setGeometry(QtCore.QRect(410, 510, 231, 121))
        self.backButton.setMinimumSize(QtCore.QSize(231, 121))
        self.backButton.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.backButton.setObjectName("backButton")
        self.stackedWidget.addWidget(self.cameraPage)
        self.classListPage = QtWidgets.QWidget()
        self.classListPage.setObjectName("classListPage")
        self.classList = QtWidgets.QWidget(self.classListPage)
        self.classList.setGeometry(QtCore.QRect(325, 110, 401, 471))
        self.classList.setObjectName("classList")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.classList)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 401, 465))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.classButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton1.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton1.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton1.setObjectName("classButton1")
        self.verticalLayout_4.addWidget(self.classButton1)
        self.classButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton2.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton2.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton2.setObjectName("classButton2")
        self.verticalLayout_4.addWidget(self.classButton2)
        self.classButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton3.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton3.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton3.setObjectName("classButton3")
        self.verticalLayout_4.addWidget(self.classButton3)
        self.classButton4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton4.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton4.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton4.setObjectName("classButton4")
        self.verticalLayout_4.addWidget(self.classButton4, 0, QtCore.Qt.AlignHCenter)
        self.classButton5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton5.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton5.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton5.setObjectName("classButton5")
        self.verticalLayout_4.addWidget(self.classButton5)
        self.classButton6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.classButton6.setMinimumSize(QtCore.QSize(259, 69))
        self.classButton6.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.classButton6.setObjectName("classButton6")
        self.verticalLayout_4.addWidget(self.classButton6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.logoutButton = QtWidgets.QPushButton(self.classListPage)
        self.logoutButton.setGeometry(QtCore.QRect(910, 10, 131, 41))
        self.logoutButton.setMinimumSize(QtCore.QSize(0, 0))
        self.logoutButton.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 15px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.logoutButton.setObjectName("logoutButton")
        self.stackedWidget.addWidget(self.classListPage)
        self.classInfoPage = QtWidgets.QWidget()
        self.classInfoPage.setObjectName("classInfoPage")
        self.frame_2 = QtWidgets.QFrame(self.classInfoPage)
        self.frame_2.setGeometry(QtCore.QRect(256, 200, 521, 241))
        self.frame_2.setStyleSheet("background-color: rgb(90, 90, 100);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(55, 10, 411, 151))
        self.frame.setMinimumSize(QtCore.QSize(271, 150))
        self.frame.setStyleSheet("background-color: rgb(136, 136, 155);\n"
"border: 3px solid rgb(124, 124, 134);\n"
"border-radius: 0px;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 205))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.timeLabel.setStyleSheet("border-width: 0px")
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout_2.addWidget(self.timeLabel, 1, 1, 1, 1)
        self.teacherMessageLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.teacherMessageLabel.setStyleSheet("border-width: 0px")
        self.teacherMessageLabel.setObjectName("teacherMessageLabel")
        self.gridLayout_2.addWidget(self.teacherMessageLabel, 3, 0, 1, 2)
        self.addressLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.addressLabel.setStyleSheet("border-width: 0px")
        self.addressLabel.setObjectName("addressLabel")
        self.gridLayout_2.addWidget(self.addressLabel, 2, 0, 1, 2)
        self.daysLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.daysLabel.setStyleSheet("border-width: 0px")
        self.daysLabel.setObjectName("daysLabel")
        self.gridLayout_2.addWidget(self.daysLabel, 1, 0, 1, 1)
        self.classNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.classNameLabel.setStyleSheet("border-width: 0px")
        self.classNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classNameLabel.setObjectName("classNameLabel")
        self.gridLayout_2.addWidget(self.classNameLabel, 0, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setStyleSheet("border-width: 0px")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 4, 0, 1, 2)
        self.backButton2 = QtWidgets.QPushButton(self.frame_2)
        self.backButton2.setGeometry(QtCore.QRect(190, 180, 141, 41))
        self.backButton2.setStyleSheet("background-color: rgb(176, 176, 195);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.backButton2.setObjectName("backButton2")
        self.stackedWidget.addWidget(self.classInfoPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.welcomeLabel = QtWidgets.QLabel(self.classListPage)
        self.welcomeLabel.setStyleSheet("background-color: rgb(136, 136, 155);\n"
"border: 3px solid rgb(124, 124, 134);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setGeometry(QtCore.QRect(325, 20, 401, 81))


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "LOG IN"))
        self.backButton.setText(_translate("MainWindow", "GO BACK"))
        self.classButton1.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.classButton2.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.classButton3.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.classButton4.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.classButton5.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.classButton6.setText(_translate("MainWindow", "Class name\n"
"\n"
"Days/Time"))
        self.logoutButton.setText(_translate("MainWindow", "LOG OUT"))
        self.timeLabel.setText(_translate("MainWindow", "Time "))
        self.teacherMessageLabel.setText(_translate("MainWindow", "Teacher\'s message"))
        self.addressLabel.setText(_translate("MainWindow", " Address"))
        self.daysLabel.setText(_translate("MainWindow", " Days"))
        self.classNameLabel.setText(_translate("MainWindow", "Class Name"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.lego.com\"><span style=\" text-decoration: underline; color:#0000ff;\">zoom link</span></a></p></body></html>"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome: name\nLogin Time: time"))
    

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="Iam65735938", database="facerecognition")
        self.cursor = self.myconn.cursor()

        self.flg_conn = False
        self.device = None
        self.classListData = []
        self.name = ""
        self.classData = []
        self.resetClassList()
        self.loginTime = None

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("train.yml")
        self.labels = {"person_name": 1}
        with open("labels.pickle", "rb") as f:
            self.labels = pickle.load(f)
            self.labels = {v: k for k, v in self.labels.items()}

        self.face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')

        self.loginButton.clicked.connect(lambda: self.loginClicked())
        self.backButton.clicked.connect(lambda: self.back1Clicked())
        self.logoutButton.clicked.connect(lambda: self.logoutClicked())
        self.classButton1.clicked.connect(lambda: self.classButtonClicked(0))
        self.classButton2.clicked.connect(lambda: self.classButtonClicked(1))
        self.classButton3.clicked.connect(lambda: self.classButtonClicked(2))
        self.classButton4.clicked.connect(lambda: self.classButtonClicked(3))
        self.classButton5.clicked.connect(lambda: self.classButtonClicked(4))
        self.classButton6.clicked.connect(lambda: self.classButtonClicked(5))
        self.backButton2.clicked.connect(lambda: self.back2Clicked())

        

    def loginClicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.connect()
        return
    
    def back1Clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.connect()
        return
    
    def back2Clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        return
    
    def logoutClicked(self):
        self.recordSession()
        self.name = ""
        self.stackedWidget.setCurrentIndex(0)
        self.loginTime = None
        return
    
    def classButtonClicked(self, buttonNumber):

        self.stackedWidget.setCurrentIndex(3)
        select = """SELECT
                        Course.course_id,
                        Course.course_code,
                        Course.course_name,
                        Course.days_of_week,
                        Course.start_time,
                        Course.end_time,
                        Course.teacher_message,
                        Course.classroom_address,
                        Course.zoom_link
                    FROM
                        Course
                    JOIN
                        Enrollment ON Course.course_id = Enrollment.course_id
                    JOIN
                        Student ON Enrollment.student_id = Student.student_id
                    WHERE
                        Student.name = '%s'""" % self.name
        
        self.cursor.execute(select)
        result = self.cursor.fetchall()
        self.classNameLabel.setText(f"{result[buttonNumber][1]} {result[buttonNumber][2]}")
        self.daysLabel.setText(f" {result[buttonNumber][3]}")
        self.timeLabel.setText(f"{result[buttonNumber][4]} {result[buttonNumber][5]} ")
        self.teacherMessageLabel.setText(f" {result[buttonNumber][6]}")
        self.addressLabel.setText(f" {result[buttonNumber][7]}")
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"{result[buttonNumber][8]}\"><span style=\" text-decoration: underline; color:#0000ff;\">zoom link</span></a></p></body></html>")

        return

    def connect(self):
        self.flg_conn = not self.flg_conn
        if self.flg_conn:
            if self.device is None:
                self.device = cv2.VideoCapture(0)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update)
            self.timer.start(50)
        else:
            if self.device is not None:
                self.device.release()
                self.device = None
            self.camFeed.clear()
            self.timer.stop()
        
        return
    



    def update(self):
        _, frame = self.device.read()
        Qframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        Qframe = QImage(Qframe, Qframe.shape[1], Qframe.shape[0], Qframe.strides[0], QImage.Format_RGB888)
        self.camFeed.setPixmap(QPixmap.fromImage(Qframe))

        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = self.recognizer.predict(roi_gray)

            # If the face is recognized
            if conf >= 40:
                # print(id_)
                # print(labels[id_])
                id = 0
                id += 1
                name = self.labels[id_]
                self.name = name
                print(name)
                self.connect()
                self.stackedWidget.setCurrentIndex(2)
                self.resetClassList()
                self.setupClassListPage()
                self.checkInOneHour()

        return
    
    def resetClassList(self):
        self.classListData = []

        self.classButton1.hide()
        self.classButton2.hide()
        self.classButton3.hide()
        self.classButton4.hide()
        self.classButton5.hide()
        self.classButton6.hide()
        return
    
    def setupClassListPage(self):


        select = """SELECT Login.login_time, Login.login_date
                        FROM Login
                        JOIN Student ON Login.student_id = Student.student_id
                        WHERE Student.name = '%s'"""% self.name
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        lastLoginInTime = result[0][0]
        lastLoginInDate = result[0][1]
        # setup welcome
        self.loginTime = datetime.now()
        # TODO add loginTime to database
        self.welcomeLabel.setText(f"Welcome: {self.name}\nCurrent Login Time: {self.loginTime.strftime('%H:%M')}\nLast Login Date: {lastLoginInDate}\nLast Login Time: {lastLoginInTime}")

        self.classListData = self.selectClassList()

        if self.classListData != []:
            for i in range(0, len(self.classListData)):
                match i:
                        case 0:
                            self.classButton1.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton1.show()
                        case 1:
                            self.classButton2.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton2.show()
                        case 2:
                            self.classButton3.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton3.show()
                        case 3:
                            self.classButton4.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton4.show()
                        case 4:
                            self.classButton5.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton5.show()
                        case 5:
                            self.classButton6.setText(f"{self.classListData[i][1]}\n{self.classListData[i][2]}\n{self.classListData[i][3]}/{self.classListData[i][4]}-{self.classListData[i][5]}")
                            self.classButton6.show()
        return
    
    


    def selectClassList(self):
        select = """SELECT
                        Course.course_id,
                        Course.course_code,
                        Course.course_name,
                        Course.days_of_week,
                        Course.start_time,
                        Course.end_time
                    FROM                                
                        Course
                    JOIN
                        Enrollment ON Course.course_id = Enrollment.course_id
                    JOIN
                        Student ON Enrollment.student_id = Student.student_id
                    WHERE
                        Student.name = '%s'""" % self.name
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    
    


    
    
    def checkInOneHour(self):
        select = """SELECT
                        Course.course_id,
                        Course.course_code,
                        Course.course_name,
                        Course.days_of_week,
                        Course.start_time,
                        Course.end_time,
                        Course.teacher_message,
                        Course.classroom_address,
                        Course.zoom_link
                    FROM
                        Course
                    JOIN
                        Enrollment ON Course.course_id = Enrollment.course_id
                    JOIN
                        Student ON Enrollment.student_id = Student.student_id
                    WHERE
                        Student.name = '%s'""" % self.name
        
        self.cursor.execute(select)
        result = self.cursor.fetchall()


        for value in result:
            print("%s",value[3])
            print("%s",value[4])
            if datetime.now().strftime("%A") in value[3] and (datetime.strptime(str(value[4]), "%H:%M:%S") - datetime.now()).seconds/3600 <= 1: 
                self.stackedWidget.setCurrentIndex(3)
                self.classNameLabel.setText(f"{value[1]} {value[2]}")
                self.daysLabel.setText(f" {value[3]}")
                self.timeLabel.setText(f"{value[4]} {value[5]} ")
                self.teacherMessageLabel.setText(f" {value[6]}")
                self.addressLabel.setText(f" {value[7]}")
                self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"{value[8]}\"><span style=\" text-decoration: underline; color:#0000ff;\">zoom link</span></a></p></body></html>")

        return
    

    def recordSession(self):
        if self.loginTime is not None:
            self.logoutTime = datetime.now()

            select = """SELECT
                            MAX(login_id)
                        FROM
                            Login;"""

            self.cursor.execute(select)
            loginID = self.cursor.fetchall()[0][0] + 1

            select = """SELECT
                            student_id
                        FROM
                            Student
                        WHERE
                            name = '%s';""" % self.name

            self.cursor.execute(select)
            userID = self.cursor.fetchall()[0][0]




            update =  "UPDATE Login SET login_date=%s, login_time=%s, logout_time=%s WHERE student_id=%s"

            login_time_str = self.loginTime.strftime('%Y-%m-%d %H:%M:%S')
            login_date_str = self.loginTime.strftime('%Y-%m-%d')
            logout_time_str = self.logoutTime.strftime('%Y-%m-%d %H:%M:%S')

            val = (login_date_str,login_time_str, logout_time_str, userID)
            self.cursor.execute(update, val)
            self.myconn.commit()

            
        return
    
    def closeEvent(self, event):
        self.myconn.close()
        self.recordSession()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
