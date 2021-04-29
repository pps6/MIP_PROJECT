from PyQt5.QtGui import QPixmap

model_data = {
    'rf_accuracy': 0.9186,
    'dt_accuracy': 0.9146,
    'knn_accuracy': 0.9146,
    'lr_accuracy': 0.9308,
    'svm_accuracy': 0.9146,
    'xgb_accuracy': 0.9430,
    'rf_score': 0.9159,
    'dt_score': 0.9156,
    'knn_score': 0.9128,
    'lr_score': 0.9317,
    'svm_score': 0.9121,
    'xgb_score': 0.9430
}

modelfullnames = {
            'svm' : 'Support Vector Machine',
            'lr' : 'Logistic Regression',
            'knn': 'K-Nearest Model',
            'rf': 'Random Forest Model',
            'xgb' : 'XGBoost Model',
            'dt':'Decision Tree Model'
        }


def template(uiWindow, model_name, fraud_cases):
    global modelfullnames, model_data
    uiWindow.modelname.setText(modelfullnames[model_name])
    uiWindow.acc_field.setText(str(model_data[model_name + "_accuracy"]))
    uiWindow.f1_field.setText(str(model_data[model_name + "_score"]))
    if len(fraud_cases) < 1:
        uiWindow.cases_label.setText("No fraud transactions found.")
    else:
        uiWindow.cases_label.setText(str(len(fraud_cases)) + " fraud transactions found.")
    pixmap = QPixmap("final_images/"+model_name+"_cm_plot.png")
    uiWindow.confusion_image.setPixmap(pixmap)

