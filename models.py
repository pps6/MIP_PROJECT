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

# print(accuracy_score(y_test, tree_yhat))
transactions = pd.read_csv('datasets/creditcard.csv',index_col=None)
processed_data = preprocessing(transactions)
# print(processed_data[1:10])
knn_output = rf_model.predict(processed_data)
# print(knn_output[knn_output==1])
result = np.where(knn_output == 1)
frauds_cases = result[0]
print(frauds_cases)
print(len(frauds_cases))

