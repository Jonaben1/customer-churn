#Import libraries
import pandas as pd
from xgboost import XGBClassifier
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('churn.csv')

# Drop customerID
df.drop(['customerID'], axis=1, inplace=True)

# Convert to int datatype

label_encoder = LabelEncoder()
obj = (df.dtypes == 'object')
for col in list(obj[obj].index):
     df[col] = label_encoder.fit_transform(df[col])


X = df.drop(['Churn'], axis=1)
Y = df.Churn

# splitting the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=7)


model = XGBClassifier(n_estimators=200, eta=0.05)


# define the datasets to evaluate each iteration
evalset = [(X_train, Y_train), (X_test, Y_test)]

# fit the model
model.fit(X_train, Y_train, eval_metric='logloss', eval_set=evalset)

# saving the trained model
pickle.dump(model, open('lg_model.pkl', 'wb'))


