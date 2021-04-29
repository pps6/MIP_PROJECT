from ui import Ui_StackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QFileDialog,QStackedWidget
from PyQt5.QtGui import QKeySequence

pagesDict = {
        'Home': 0,
        'Output':1
}

filename = ""
models_selected = []

class MainWindow(QStackedWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.uiWindow = Ui_StackedWidget()
        self.startUIWindow()
        self.maintain_operations()
        self.show()


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
        if self..isChecked():


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
