from ui import Ui_stackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QFileDialog,QStackedWidget
from models import predict 
from model_out_template import template,createGraph,dashboard_template
from PyQt5.QtGui import QPixmap
from pdf import create_pdf

pagesDict = {
        'Home': 0,
        'Output':1
}

filename = ""
output = ""
algos_selected = []
shortnames = {
            'Support Vector Machine':'svm',
            'Logistic Regression':'lr',
            'K-Nearest Model':'knn',
            'Random Forest Model':'rf',
            'XGBoost Model':'xgb',
            'Decision Tree Model':'dt'
        }

# Fraud Transaction Intersection of all Models
results_intersection = []


class MainWindow(QStackedWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.uiWindow = Ui_stackedWidget()
        self.startUIWindow()
        self.btns = [self.uiWindow.btn1_out,self.uiWindow.btn2_out,self.uiWindow.btn3_out,
                     self.uiWindow.btn4_out,self.uiWindow.btn5_out,self.uiWindow.btn6_out]
        self.setCurrentIndex(0)
        self.maintain_operations()
        self.show()
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
        # self.uiWindow.Back.clicked.connect(lambda : self.setCurrentIndex(pagesDict['Home']))
        # self.uiWindow.run.clicked.connect(lambda: self.setCurrentIndex(pagesDict['Output']))

    def show_info_popup(self,message):
        msg = QMessageBox()
        msg.show()
        height = self.height()
        width = self.width()
        msg.move(( width - msg.width() )//2,height//2)
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
        global shortnames,output
        self.uiWindow.file_select.clicked.connect(lambda: self.file_dialog_open())
        self.uiWindow.run.clicked.connect(lambda: self.run_clicked())
        self.uiWindow.Back.clicked.connect(lambda: self.back_clicked())
        self.uiWindow.btn1_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn1_out))
        self.uiWindow.btn2_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn2_out))
        self.uiWindow.btn3_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn3_out))
        self.uiWindow.btn4_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn4_out))
        self.uiWindow.btn5_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn5_out))
        self.uiWindow.btn6_out.clicked.connect(lambda: self.model_clicked(self.uiWindow.btn6_out))
        self.uiWindow.dashboard_out.clicked.connect(lambda : self.dashboard_clicked(self.uiWindow.dashboard_out))
        self.uiWindow.download.clicked.connect(lambda:self.download_clicked())
        header = self.uiWindow.results_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # for i in self.btns:
        #     # print(i.text())
        #     i.clicked.connect(lambda: self.model_clicked(i))
        # self.uiWindow.shade_opening_add_clear.clicked.connect(lambda: clear.clear_shade_opening_add(self))

    def file_dialog_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, "Select Dataset", "",
                                                  "CSV Files (*.csv)", options=options)
        if filename:
            self.uiWindow.file_name.setText(filename)

    def run_clicked(self):
        global filename, output
        global algos_selected
        if self.uiWindow.svm_select.isChecked():
            algos_selected.append('svm')
        if self.uiWindow.dt_select.isChecked():
            algos_selected.append('dt')
        if self.uiWindow.xgb_select.isChecked():
            algos_selected.append('xgb')
        if self.uiWindow.lr_select.isChecked():
            algos_selected.append('lr')
        if self.uiWindow.knn_select.isChecked():
            algos_selected.append('knn')
        if self.uiWindow.rf_select.isChecked():
            algos_selected.append('rf')
        common_fraud_cases = []
        if len(algos_selected) > 0 and filename != "":
            createGraph(algos_selected)
            pixmap_f1 = QPixmap("./images/f1_graph.png")
            pixmap_acc = QPixmap('./images/acc_graph.png')
            self.uiWindow.acc_bar_plot.setPixmap(pixmap_f1)
            self.uiWindow.confusion_image.setPixmap(pixmap_acc)
            output = predict(filename,algos_selected)
            output_res = [i['output'] for i in output]
            global results_intersection
            results_intersection = set(output_res[0]).intersection(*output_res[1:])
            print(len(results_intersection),results_intersection)
            self.setCurrentIndex(pagesDict['Output'])
            for index,i in enumerate(algos_selected):
                self.btns[index].setText(self.modelnames[i])
            for i in range(len(algos_selected),6):
                self.btns[i].hide()
            self.dashboard_clicked(self.uiWindow.dashboard_out)
            algos_selected = []
        else:
            self.show_warning_info("No file or model selected")
        algos_selected = []


    def back_clicked(self):
        global algos_selected
        algos_selected = []
        self.setCurrentIndex(pagesDict['Home'])
        for i in self.btns:
            i.show()

    def dashboard_clicked(self,i):
        self.uiWindow.acc_bar_plot.show()
        self.uiWindow.modelname.setText('Dashboard')
        pixmap = QPixmap("./images/acc_graph.png")
        self.uiWindow.confusion_image.setPixmap(pixmap)
        global results_intersection,filename
        self.uiWindow.cases_label.setText(f'{str(len(results_intersection))} fraud transactions found.')
        dashboard_template(self.uiWindow,results_intersection,filename)


    def model_clicked(self, i):
        # print("model_clicked")
        global filename
        self.setCurrentIndex(pagesDict['Output'])
        global output,shortnames
        print(i.text())
        model_name = shortnames[i.text()]
        for j in output:
            if j['model_name'] == model_name:
                fraud_cases = j['output']
                break
        template(self.uiWindow,model_name,fraud_cases,filename)

    def download_clicked(self):
        global filename,results_intersection
        output_filename = create_pdf(filename,results_intersection)
        self.show_info_popup(f"Output Saved to {output_filename}")

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
