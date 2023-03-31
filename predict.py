import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# load the train model
with open('xgb_model.pkl', 'rb') as xgb:
    model = pickle.load(xgb)




def prediction(gender, SeniorCitizen, Partner, Dependents, tenure,PhoneService, MultipleLines,
               InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
               StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
           MonthlyCharges, TotalCharge):

    '''Get the input from the user. Turn to Pandas DataFrame, encode,  and make prediction.
    Then, return results'''

    data = {'gender': gender, 'SeniorCitizen': SeniorCitizen, 'Partner': Partner, 'Dependents': Dependents,
        'tenure': tenure, 'PhoneService': PhoneService, 'MultipleLines': MultipleLines,  'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity, 'OnlineBackup': OnlineBackup, 'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport, 'StreamingTV': StreamingTV, 'StreamingMovies': StreamingMovies,
        'Contract': Contract, 'PaperlessBilling': PaperlessBilling, 'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges, 'TotalCharges': TotalCharge}
    df = pd.DataFrame(data, index=[1])
    label_encoder = LabelEncoder()
    # converting to int data type
    obj = (df.dtypes == 'object')
    for i in obj[obj].index:
        df[i] = label_encoder.fit_transform(df[i])

    # making predictions using the train model
    result = model.predict(df)
    return result
