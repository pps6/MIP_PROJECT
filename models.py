import joblib
import pandas as pd
from preprocessing import preprocessing
import numpy as np

loaded_model = joblib.load('models/rf.sav')
transactions = pd.read_csv('data_part5.csv',index_col=0)
processed_data = preprocessing(transactions)
# print(processed_data[1:10])
knn_output = loaded_model.predict(processed_data)
# print(knn_output[knn_output==1])
result = np.where(knn_output == 1)
frauds_cases = result[0]
print(frauds_cases)
print(len(frauds_cases))

