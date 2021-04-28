from sklearn.preprocessing import StandardScaler

def preprocessing(transactions):
  transactions.drop('Time', axis = 1, inplace = True)
  sc = StandardScaler()
  amount = transactions['Amount'].values

  transactions['Amount'] = sc.fit_transform(amount.reshape(-1, 1))
  X = transactions.drop('Class', axis = 1).values
  return X

