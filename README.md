Churn prediction app using a dataset sourced by the IBM Developer Platform.
The dataset has 7043 rows and 21 features.

There are 17 categorical features:

CustomerID: Customer ID unique for each customer
gender: Whether the customer is a male or a female
SeniorCitizen: Whether the customer is a senior citizen or not (1, 0)
Partner: Whether the customer has a partner or not (Yes, No)
Dependent: Whether the customer has dependents or not (Yes, No)
PhoneService: Whether the customer has a phone service or not (Yes, No)
MultipeLines: Whether the customer has multiple lines or not (Yes, No, No phone service)
InternetService: Customer’s internet service provider (DSL, Fiber optic, No)
OnlineSecurity: Whether the customer has online security or not (Yes, No, No internet service)
OnlineBackup: Whether the customer has an online backup or not (Yes, No, No internet service)
DeviceProtection: Whether the customer has device protection or not (Yes, No, No internet service)
TechSupport: Whether the customer has tech support or not (Yes, No, No internet service)
StreamingTV: Whether the customer has streaming TV or not (Yes, No, No internet service)
StreamingMovies: Whether the customer has streaming movies or not (Yes, No, No internet service)
Contract: The contract term of the customer (Month-to-month, One year, Two years)
PaperlessBilling: The contract term of the customer (Month-to-month, One year, Two years)
PaymentMethod: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))

Next, there are 3 numerical features:

Tenure: Number of months the customer has stayed with the company
MonthlyCharges: The amount charged to the customer monthly
TotalCharges: The total amount charged to the customer
Finally, there’s a prediction feature:

Churn: Whether the customer churned or not (Yes or No)

We used XGBoost model to train the data. It achieved an accuracy score of 80.4%.
