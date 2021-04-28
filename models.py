from sklearn.metrics import accuracy_score # evaluation metric
from sklearn.metrics import f1_score # evaluation metric
import joblib
import pandas as pd
from preprocessing import preprocessing
import numpy as np

rf_model = joblib.load('models/rf.sav')
dt_model = joblib.load('models/decision_tree.sav')
knn_model = joblib.load('models/knn.sav')
lr_model = joblib.load('models/lr.sav')
svm_model = joblib.load('models/svm.sav')
# xgb_model = joblib.load('models/xgb.sav')

transactions = pd.read_csv('datasets/data_part5.csv',index_col=0)
processed_data = preprocessing(transactions)
# print(processed_data[1:10])
knn_output = rf_model.predict(processed_data)
# print(knn_output[knn_output==1])
result = np.where(knn_output == 1)
frauds_cases = result[0]
print(frauds_cases)
print(len(frauds_cases))

