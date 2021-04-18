# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.alg1 = QtWidgets.QPushButton(self.centralwidget)
        self.alg1.setGeometry(QtCore.QRect(40, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alg1.setFont(font)
        self.alg1.setObjectName("alg1")
        self.alg2 = QtWidgets.QPushButton(self.centralwidget)
        self.alg2.setGeometry(QtCore.QRect(40, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alg2.setFont(font)
        self.alg2.setObjectName("alg2")
        self.alg3 = QtWidgets.QPushButton(self.centralwidget)
        self.alg3.setGeometry(QtCore.QRect(40, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.alg3.setFont(font)
        self.alg3.setObjectName("alg3")
        self.alg4 = QtWidgets.QPushButton(self.centralwidget)
        self.alg4.setGeometry(QtCore.QRect(40, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.alg4.setFont(font)
        self.alg4.setObjectName("alg4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 550, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(310, 100, 531, 381))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 508, 358))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Output by selected Algorithm"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.alg1.setText(_translate("MainWindow", "Algo 1"))
        self.alg2.setText(_translate("MainWindow", "Algo 2"))
        self.alg3.setText(_translate("MainWindow", "Algo 3"))
        self.alg4.setText(_translate("MainWindow", "Algo 4"))
        self.pushButton.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
