from ui import Ui_StackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QFileDialog,QStackedWidget
from PyQt5.QtGui import QKeySequence
from models import predict 

pagesDict = {
        'Home': 0,
        'Output':1
}

filename = ""
algos_selected = []

class MainWindow(QStackedWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.uiWindow = Ui_StackedWidget()
        self.startUIWindow()
        self.maintain_operations()
        self.show()
        self.btns = [self.uiWindow.btn1_out,self.uiWindow.btn2_out,self.uiWindow.btn3_out,self.uiWindow.btn4_out,self.uiWindow.btn5_out,self.uiWindow.btn6_out]
        self.modelnames = {
            'svm' : 'Support Vector Machine',
            'lr' : 'Logistic Regression',
            'knn': 'K-Nearest Model',
            'rf': 'Random Forest Model',
            'xgb' : 'XGBoost Model',
            'dt':'Decision Tree Model'
        }
        


    def startUIWindow(self):
        self.uiWindow.setupUi(self)
        self.uiWindow.Back.clicked.connect(lambda : self.setCurrentIndex(pagesDict['Home']))

    def show_info_popup(self,message):
        #TODO change icon
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def show_warning_info(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_() 

    def maintain_operations(self):
        self.uiWindow.file_select.clicked.connect(lambda: self.file_dialog_open())
        self.uiWindow.run.clicked.connect(lambda: self.run_clicked())
        # self.uiWindow.shade_opening_add_clear.clicked.connect(lambda: clear.clear_shade_opening_add(self))
        # self.uiWindow.shade_opening_modify_clear.clicked.connect(lambda: clear.clear_shade_opening_modify(self))
        # self.uiWindow.shade_opening_delete_clear.clicked.connect(lambda: clear.clear_shade_opening_delete(self))
        # self.uiWindow.shade_opening_view_clear.clicked.connect(lambda: clear.clear_shade_opening_view(self))
        # self.uiWindow.colour_closing_stock_table.cellChanged.connect(lambda row, column: operations_callbacks.display_product_name(row, column, self, 0,

    def file_dialog_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, "Select Dataset", "",
                                                  "CSV Files (*.csv)", options=options)
        if filename:
            self.uiWindow.file_name.setText(filename)

    def run_clicked(self):
        global algos_selected
        if self.uiWindow.svm_select.isChecked():
            algos_selected.append('svm')
        if self.uiWindow.dt_select.isChecked():
            algos_selected.append('dt')
        if self.uiWindow.lr_select.isChecked():
            algos_selected.append('lr')
        if self.uiWindow.knn_select.isChecked():
            algos_selected.append('knn')
        if self.uiWindow.rf_select.isChecked():
            algos_selected.append('rf')
        output = predict(filename,algos_selected)
        self.uiWindow.setCurrentIndex(pagesDict['Output'])
        for index,i in enumerate(algos_selected):
            self.btns[index].setText(self.modelname[i])
        for i in range(len(algos_selected),7):
            self.btn[index].hide()



if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
