from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def template(uiWindow, model_name, fraud_cases,filename):
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
    transactions = pd.read_csv(filename, index_col=None)
    subset = transactions[["Time","Amount"]]
    x = subset.loc[fraud_cases,:]
    # x['Index'] = fraud_cases
    x.reset_index(inplace=True)
    # print(x.head())
    x = np.array(x)
    for row in range(0,len(x)):
        uiWindow.results_table.insertRow(row)
        for column in range(0,3):
            uiWindow.results_table.setItem(row, column,
                                           QtWidgets.QTableWidgetItem(
                                               str(x[row,column])))

def createGraph(models):
    
    frequencies_acc = [model_data[i + '_accuracy'] for i in models]
    frequencies_f1 = [model_data[i + '_score'] for i in models]



    freq_series_acc = pd.Series(frequencies_acc)
    freq_series_f1 = pd.Series(frequencies_f1) 

    x_labels = [modelfullnames[i] for i in models]



    # Plot the figure.
    plt.figure(figsize=(12, 8))
    ax = freq_series_acc.plot(kind='bar')
    ax.set_title('Accuracy Scores')
    ax.set_xlabel('Models')
    ax.set_ylabel('Accuary')
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    # Make some labels.
    labels_acc = [round(i,2) for i in frequencies_acc]

    for index,data in enumerate(labels_acc):
        # height = rect.get_height()
        ax.text(index,data+0.01,data,
                ha='center', va='bottom')

    plt.savefig('images/acc_graph.png',bbox_inches='tight') 
    # F1 Score
    plt.figure(figsize=(12, 8))
    ax = freq_series_f1.plot(kind='bar')
    ax.set_title('F1 Scores')
    ax.set_xlabel('Models')
    ax.set_ylabel('F1 Scores')
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    # Make some labels.
    labels_f1 = [round(i,2) for i in frequencies_f1]

    for index,data in enumerate(labels_f1):
        # height = rect.get_height()
        ax.text(index,data+0.01,data,
                ha='center', va='bottom')

    plt.savefig('images/f1_graph.png',bbox_inches='tight') 
