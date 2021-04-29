from sklearn.metrics import accuracy_score # evaluation metric
from sklearn.metrics import f1_score # evaluation metric
import joblib
import pandas as pd
from preprocessing import preprocessing
import numpy as np

rf_model = joblib.load('models_final/rf.sav')
dt_model = joblib.load('models_final/decision_tree.sav')
knn_model = joblib.load('models_final/knn.sav')
lr_model = joblib.load('models_final/lr.sav')
svm_model = joblib.load('models_final/svm.sav')
xgb_model = joblib.load('models_final/xgb.sav')

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

# print(accuracy_score(y_test, tree_yhat))

def getFraudCases(model,data):
    output = model.predict(data)
    result = np.where(output == 1)
    frauds_cases = result[0]
    print(frauds_cases)
    print(len(frauds_cases))
    return frauds_cases



def predict(datasetFile,models_selected):
    transactions = pd.read_csv(datasetFile,index_col=None)
    processed_data = preprocessing(transactions)
    # print(processed_data[1:10]
    getCases = lambda x:getFraudCases(x,processed_data)
    
    output_res []

    for i in models_selected:
        if i == 'svm':
            fraud_cases = getCases(svm_model)   
        if i == 'rf':
            fraud_cases = getCases(rf_model)
        if i == 'dt':
            fraud_cases = getCases(dt_model)
        if i == 'knn':
            fraud_cases = getCases(knn_model)
        if i == 'xgb':
            fraud_cases = getCases(xgb_model)
        if i == 'lr':
            fraud_cases = getCases(lr_model)
        output_res.append({
            'model_name':i,
            'output':fraud_cases
        })
    # print(knn_output[knn_output==1])
