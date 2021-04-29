# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1299, 951)
        self.HomePage = QtWidgets.QWidget()
        self.HomePage.setObjectName("HomePage")
        self.file_select = QtWidgets.QPushButton(self.HomePage)
        self.file_select.setGeometry(QtCore.QRect(870, 280, 121, 31))
        self.file_select.setObjectName("file_select")
        self.run = QtWidgets.QPushButton(self.HomePage)
        self.run.setGeometry(QtCore.QRect(820, 780, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.run.setFont(font)
        self.run.setObjectName("run")
        self.dt_select = QtWidgets.QCheckBox(self.HomePage)
        self.dt_select.setGeometry(QtCore.QRect(330, 500, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dt_select.setFont(font)
        self.dt_select.setObjectName("dt_select")
        self.svm_select = QtWidgets.QCheckBox(self.HomePage)
        self.svm_select.setGeometry(QtCore.QRect(330, 450, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.svm_select.setFont(font)
        self.svm_select.setChecked(False)
        self.svm_select.setObjectName("svm_select")
        self.rf_select = QtWidgets.QCheckBox(self.HomePage)
        self.rf_select.setGeometry(QtCore.QRect(330, 700, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rf_select.setFont(font)
        self.rf_select.setObjectName("rf_select")
        self.xgb_select = QtWidgets.QCheckBox(self.HomePage)
        self.xgb_select.setGeometry(QtCore.QRect(330, 550, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.xgb_select.setFont(font)
        self.xgb_select.setObjectName("xgb_select")
        self.label_2 = QtWidgets.QLabel(self.HomePage)
        self.label_2.setGeometry(QtCore.QRect(380, 160, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.knn_select = QtWidgets.QCheckBox(self.HomePage)
        self.knn_select.setGeometry(QtCore.QRect(330, 650, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.knn_select.setFont(font)
        self.knn_select.setObjectName("knn_select")
        self.label_3 = QtWidgets.QLabel(self.HomePage)
        self.label_3.setGeometry(QtCore.QRect(320, 400, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.HomePage)
        self.label.setGeometry(QtCore.QRect(320, 270, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lr_select = QtWidgets.QCheckBox(self.HomePage)
        self.lr_select.setGeometry(QtCore.QRect(330, 600, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lr_select.setFont(font)
        self.lr_select.setObjectName("lr_select")
        self.file_name = QtWidgets.QLineEdit(self.HomePage)
        self.file_name.setEnabled(False)
        self.file_name.setGeometry(QtCore.QRect(490, 280, 351, 32))
        self.file_name.setObjectName("file_name")
        StackedWidget.addWidget(self.HomePage)
        self.OutputPage = QtWidgets.QWidget()
        self.OutputPage.setObjectName("OutputPage")
        self.btn2_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn2_out.setGeometry(QtCore.QRect(60, 300, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn2_out.setFont(font)
        self.btn2_out.setObjectName("btn2_out")
        self.download = QtWidgets.QPushButton(self.OutputPage)
        self.download.setGeometry(QtCore.QRect(870, 860, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.btn6_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn6_out.setGeometry(QtCore.QRect(60, 570, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn6_out.setFont(font)
        self.btn6_out.setObjectName("btn6_out")
        self.btn1_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn1_out.setGeometry(QtCore.QRect(60, 230, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn1_out.setFont(font)
        self.btn1_out.setObjectName("btn1_out")
        self.btn4_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn4_out.setGeometry(QtCore.QRect(60, 440, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn4_out.setFont(font)
        self.btn4_out.setObjectName("btn4_out")
        self.Back = QtWidgets.QPushButton(self.OutputPage)
        self.Back.setGeometry(QtCore.QRect(90, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.scrollArea = QtWidgets.QScrollArea(self.OutputPage)
        self.scrollArea.setGeometry(QtCore.QRect(340, 120, 921, 701))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.display = QtWidgets.QWidget()
        self.display.setGeometry(QtCore.QRect(0, 0, 896, 676))
        self.display.setObjectName("display")
        self.label_5 = QtWidgets.QLabel(self.display)
        self.label_5.setGeometry(QtCore.QRect(160, 180, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.results_table = QtWidgets.QTableView(self.display)
        self.results_table.setGeometry(QtCore.QRect(0, 530, 901, 151))
        self.results_table.setObjectName("results_table")
        self.acc_field = QtWidgets.QLineEdit(self.display)
        self.acc_field.setGeometry(QtCore.QRect(250, 190, 91, 51))
        self.acc_field.setAutoFillBackground(False)
        self.acc_field.setObjectName("acc_field")
        self.modelname = QtWidgets.QLabel(self.display)
        self.modelname.setGeometry(QtCore.QRect(10, 20, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.modelname.setFont(font)
        self.modelname.setAlignment(QtCore.Qt.AlignCenter)
        self.modelname.setObjectName("modelname")
        self.label_7 = QtWidgets.QLabel(self.display)
        self.label_7.setGeometry(QtCore.QRect(160, 250, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.f1_field = QtWidgets.QLineEdit(self.display)
        self.f1_field.setGeometry(QtCore.QRect(250, 260, 91, 51))
        self.f1_field.setObjectName("f1_field")
        self.cases_label = QtWidgets.QLabel(self.display)
        self.cases_label.setGeometry(QtCore.QRect(50, 380, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cases_label.setFont(font)
        self.cases_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cases_label.setObjectName("cases_label")
        self.confusion_image = QtWidgets.QLabel(self.display)
        self.confusion_image.setGeometry(QtCore.QRect(450, 50, 431, 431))
        self.confusion_image.setText("")
        self.confusion_image.setPixmap(QtGui.QPixmap("ui/../final_images/tree_cm_plot.png"))
        self.confusion_image.setObjectName("confusion_image")
        self.scrollArea.setWidget(self.display)
        self.btn3_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn3_out.setGeometry(QtCore.QRect(60, 370, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn3_out.setFont(font)
        self.btn3_out.setObjectName("btn3_out")
        self.btn5_out = QtWidgets.QPushButton(self.OutputPage)
        self.btn5_out.setGeometry(QtCore.QRect(60, 510, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn5_out.setFont(font)
        self.btn5_out.setObjectName("btn5_out")
        self.dashboard_out = QtWidgets.QPushButton(self.OutputPage)
        self.dashboard_out.setGeometry(QtCore.QRect(60, 160, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dashboard_out.setFont(font)
        self.dashboard_out.setObjectName("dashboard_out")
        self.label_4 = QtWidgets.QLabel(self.OutputPage)
        self.label_4.setGeometry(QtCore.QRect(350, 50, 631, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        StackedWidget.addWidget(self.OutputPage)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.file_select.setText(_translate("StackedWidget", "choose file"))
        self.run.setText(_translate("StackedWidget", "Run"))
        self.dt_select.setText(_translate("StackedWidget", "  Decision Tree Model"))
        self.svm_select.setText(_translate("StackedWidget", "  Support Vector Machine"))
        self.rf_select.setText(_translate("StackedWidget", "  Random Forest Tree"))
        self.xgb_select.setText(_translate("StackedWidget", "  XGBoost Model"))
        self.label_2.setText(_translate("StackedWidget", "Credit Card Fraud Transaction Detection"))
        self.knn_select.setText(_translate("StackedWidget", "  K-Nearest Neighbour"))
        self.label_3.setText(_translate("StackedWidget", "Select the algorithm"))
        self.label.setText(_translate("StackedWidget", "Choose the file"))
        self.lr_select.setText(_translate("StackedWidget", "  Logistic Regression"))
        self.file_name.setText(_translate("StackedWidget", "Choose a csv file"))
        self.btn2_out.setText(_translate("StackedWidget", "Decision Tree Model"))
        self.download.setText(_translate("StackedWidget", "Download"))
        self.btn6_out.setText(_translate("StackedWidget", " Random Forest Tree"))
        self.btn1_out.setText(_translate("StackedWidget", "Support Vector Machine"))
        self.btn4_out.setText(_translate("StackedWidget", "Logistic Regression"))
        self.Back.setText(_translate("StackedWidget", "Back"))
        self.label_5.setText(_translate("StackedWidget", "  Accuracy"))
        self.modelname.setText(_translate("StackedWidget", "TextLabel"))
        self.label_7.setText(_translate("StackedWidget", "F1 - Score"))
        self.cases_label.setText(_translate("StackedWidget", "Total"))
        self.btn3_out.setText(_translate("StackedWidget", "XGBoost Model"))
        self.btn5_out.setText(_translate("StackedWidget", " K-Nearest Neighbour"))
        self.dashboard_out.setText(_translate("StackedWidget", "Dashboard"))
        self.label_4.setText(_translate("StackedWidget", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
