from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import mvc.view.resources_rc as resources_rc
from mvc.view.ui_config import MAIN_MENU_DARK

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.MainWindow = MainWindow
        MainWindow.resize(939, 631)
        MainWindow.setStyleSheet(MAIN_MENU_DARK)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionUkrainian = QAction(MainWindow)
        self.actionUkrainian.setObjectName(u"actionUkrainian")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.header_nav = QFrame(self.centralwidget)
        self.header_nav.setObjectName(u"header_nav")
        self.header_nav.setGeometry(QRect(0, 0, 931, 81))
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.header_nav)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 10, 181, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label1 = QLabel(self.frame_2)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(0, 10, 171, 41))
        font = QFont()
        font.setFamily(u"./view/fonts/Nova_Flat/NovaFlat-Regular.ttf")
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet(u"QLabel#label1{\n"
            "	font-size: 20px;\n"
        "}")
        self.controlButtons = QFrame(self.header_nav)
        self.controlButtons.setObjectName(u"controlButtons")
        self.controlButtons.setGeometry(QRect(630, 10, 281, 61))
        self.controlButtons.setFrameShape(QFrame.StyledPanel)
        self.controlButtons.setFrameShadow(QFrame.Raised)
        self.QPushButton = QPushButton(self.controlButtons)
        self.QPushButton.setObjectName(u"QPushButton")
        self.QPushButton.setGeometry(QRect(10, 10, 101, 41))

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 90, 431, 531))
        self.frame_3.setStyleSheet(u"QLabel#label_2, QLabel#label_3, QLabel#label_4, QLabel#label_5 {\n"
            " line-height: 1.5\n"
        "}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet(u"QLabel#label_2, QLabel#label_3, QLabel#label_4, QLabel#label_5 {\n"
" line-height: 1.5\n"
"}")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 381, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel#label{\n"
"	font-size: 18px;\n"
"}")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 401, 51))
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 411, 61))
        
        font1 = QFont()
        font1.setFamily(u"./Nova_Flat/NovaFlat-Regular.ttf")
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 401, 71))
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 270, 401, 71))
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 360, 381, 41))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel#label_6{\n"
"	font-size: 16px;\n"
"}")
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 400, 381, 41))
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 440, 381, 41))
        self.label_9.setTextFormat(Qt.PlainText)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(460, 90, 471, 531))
        self.frame_5.setStyleSheet(u"QPushButton#clearCache, QPushButton#clearModel, QPushButton#convertCSV,\n"
"QPushButton#convertPDF, QPushButton#fetchButton {\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"QPushButton#clearCache, QPushButton#clearModel, QPushButton#convertCSV,\n"
"QPushButton#convertPDF, QPushButton#fetchButton :hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 10, 381, 41))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel#label_10{\n"
"	font-size: 18px;\n"
"}")
        self.label_10.setTextFormat(Qt.PlainText)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 50, 231, 41))
        self.label_11.setStyleSheet(u"QLabel#label_11{\n"
"	font-size: 15px;\n"
"}")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.fetchButton = QPushButton(self.frame_5)
        self.fetchButton.setObjectName(u"fetchButton")
        self.fetchButton.setGeometry(QRect(60, 100, 111, 41))
        self.fetchButton.setStyleSheet(u"#fetchButton {\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#fetchButton:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(190, 100, 111, 41))
        self.label_15.setTextFormat(Qt.PlainText)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 210, 181, 41))
        self.label_12.setStyleSheet(u"QLabel#label_12{\n"
"	font-size: 15px;\n"
"}")
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.timeIntervals = QComboBox(self.frame_5)
        self.timeIntervals.addItem("")
        self.timeIntervals.addItem("")
        self.timeIntervals.addItem("")
        self.timeIntervals.addItem("")
        self.timeIntervals.setObjectName(u"timeIntervals")
        self.timeIntervals.setGeometry(QRect(200, 260, 111, 31))
        self.timeIntervals.setStyleSheet(u"QComboBox#timeIntervals{\n"
"	border: 1px solid #fff;\n"
"    border-radius: 5px;\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"\n"
"QComboBox#timeIntervals QAbstractItemView {\n"
"	color: 000;\n"
"}")
        self.timeIntervals.setPlaceholderText(u"")
        self.spinBox = QSpinBox(self.frame_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(60, 260, 101, 31))
        self.spinBox.setStyleSheet(u"QSpinBox#spinBox{\n"
"	 border: 1px solid #fff;\n"
"    border-radius: 5px;\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"    padding: 5px; /* Adjust as needed */\n"
"}")
        self.spinBox.setMinimum(2)
        self.clearCache = QPushButton(self.frame_5)
        self.clearCache.setObjectName(u"clearCache")
        self.clearCache.setGeometry(QRect(60, 160, 111, 41))
        self.clearCache.setStyleSheet(u"#clearCache {\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#clearCache:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 300, 161, 41))
        self.label_13.setStyleSheet(u"QLabel#label_13{\n"
"	font-size: 15px;\n"
"}")
        self.label_13.setTextFormat(Qt.PlainText)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.predictPrices = QPushButton(self.frame_5)
        self.predictPrices.setObjectName(u"predictPrices")
        self.predictPrices.setGeometry(QRect(60, 350, 101, 41))
        self.predictPrices.setStyleSheet(u"QPushButton#predictPrices{\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"QPushButton#predictPrices:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")    
        self.clearModel = QPushButton(self.frame_5)
        self.clearModel.setObjectName(u"clearModel")
        self.clearModel.setGeometry(QRect(220, 350, 111, 41))
        self.clearModel.setStyleSheet(u"QPushButton#clearModel{\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"QPushButton#clearModel:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.convertCSV = QPushButton(self.frame_5)
        self.convertCSV.setObjectName(u"convertCSV")
        self.convertCSV.setGeometry(QRect(60, 450, 111, 41))
        self.convertCSV.setStyleSheet(u"#convertCSV {\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#convertCSV:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")    
        self.convertPDF = QPushButton(self.frame_5)
        self.convertPDF.setObjectName(u"convertPDF")
        self.convertPDF.setGeometry(QRect(250, 450, 111, 41))
        self.convertPDF.setStyleSheet(u"#convertPDF {\n"
"	background-color: rgb(61, 80, 120);\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#convertPDF:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 400, 171, 41))
        self.label_14.setStyleSheet(u"QLabel#label_14{\n"
"	font-size: 15px;\n"
"}")
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(40, 400, 351, 121))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.fetchButton.raise_()
        self.label_15.raise_()
        self.label_12.raise_()
        self.timeIntervals.raise_()
        self.spinBox.raise_()
        self.clearCache.raise_()
        self.label_13.raise_()
        self.predictPrices.raise_()
        self.clearModel.raise_()
        self.convertCSV.raise_()
        self.convertPDF.raise_()
        self.label_14.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.timeIntervals.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light mode", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionUkrainian.setText(QCoreApplication.translate("MainWindow", u"Ukrainian", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"MAIN MENU", None))
        self.QPushButton.setText(QCoreApplication.translate("MainWindow", u"Light mode", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2. Choose a certain time interval to predict prices. You can choose for several days, weeks, months and years. By default you predict for 2 days.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1. Download the data from API. After downloading the data your result will be stored in cache. You can clear cache manually by pressign \"Clear cache\" button which will appear after response.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"3. Now it is time to predict prices. Press the \"Predict\" button to start modeling data and creating a full report of the preidction. You will see results in the new window where you can navigate through charts by sidebar to see the results.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4. In addition to previous stage, the program stores model fitting results in cache to deal with the same data faster in the next time. Of course you have an opportunity to clear cache manually by pressing \"Clear model\" button.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Extra", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1. You have two options what to do with results. First one is about creating .csv file which consists of prediction results", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2. Second one creates PDF report which displays all charts ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Load the data from the server", None))
        self.fetchButton.setText(QCoreApplication.translate("MainWindow", u"Fetch", None))
        self.label_15.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Choose the interval", None))
        self.timeIntervals.setItemText(0, QCoreApplication.translate("MainWindow", u"days", None))
        self.timeIntervals.setItemText(1, QCoreApplication.translate("MainWindow", u"weeks", None))
        self.timeIntervals.setItemText(2, QCoreApplication.translate("MainWindow", u"months", None))
        self.timeIntervals.setItemText(3, QCoreApplication.translate("MainWindow", u"years", None))

        self.timeIntervals.setCurrentText(QCoreApplication.translate("MainWindow", u"days", None))
        self.clearCache.setText(QCoreApplication.translate("MainWindow", u"Clear cache", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Predict prices", None))
        self.predictPrices.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.clearModel.setText(QCoreApplication.translate("MainWindow", u"Clear model", None))
        self.convertCSV.setText(QCoreApplication.translate("MainWindow", u"Convert to CSV", None))
        self.convertPDF.setText(QCoreApplication.translate("MainWindow", u"Convert to PDF", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Optional", None))
    # retranslateUi

