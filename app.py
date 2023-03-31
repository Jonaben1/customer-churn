import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from predict import prediction

def main():
    st.header('Customer Churn Prediction App')

    # displaying image
    image = Image.open('executives.jpg')
    st.sidebar.image(image)

    st.sidebar.info('This Streamlit app predicts customer churn for a fictional telecommunication company')
    st.sidebar.info('Get in touch if you need something similar tailored to your use case')

    st.subheader("Demographic Data")
    left, right = st.columns((2,2))

    gender = left.selectbox('Gender', ['Male', 'Female'])
    seniorcitizen = right.selectbox('Senior Citizen:', ['Yes', 'No'])
    dependents = left.selectbox('Dependent:', ['Yes', 'No'])
    partner = right.selectbox('Partner', ['Yes', 'No'])

    st.subheader("Payment Data")

    left, right = st.columns((2, 2))
    tenure = left.slider('Tenure: Number of months the customer has stayed with the company', min_value=0, max_value=72, value=0)
    contract = right.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    paperlessbilling = left.selectbox('Paperless Billing', ['Yes', 'No'])
    PaymentMethod = right.selectbox('PaymentMethod', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])
    monthlycharges = left.number_input('The amount charged to the customer monthly ($)', min_value=0, max_value=150, value=0)
    totalcharges = right.number_input('The total amount charged to the customer ($)',min_value=0, max_value=10000, value=0)

    st.subheader("Services Rendered")

    left, right = st.columns((2,2))
    multiplelines = left.selectbox("Does the customer have multiple lines",['Yes','No','No phone service'])
    phoneservice = right.selectbox('Phone Service:', ['Yes', 'No'])
    internetservice = left.selectbox("Does the customer have internet service", ['DSL', 'Fiber optic', 'No'])
    deviceprotection = right.selectbox("Does the customer have online security", ['Yes','No','No internet service'])
    onlinesecurity = right.selectbox("Does the customer have device protection", ['Yes','No','No internet service'])
    onlinebackup = left.selectbox("Does the customer have online backup", ['Yes','No','No internet service'])
    techsupport = right.selectbox("Does the customer have technology support", ['Yes','No','No internet service'])
    streamingtv = left.selectbox("Does the customer stream TV", ['Yes','No','No internet service'])
    streamingmovies = right.selectbox("Does the customer stream movies", ['Yes','No','No internet service'])

    predict = prediction(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines,
               internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
               streamingtv, streamingmovies, contract, paperlessbilling, PaymentMethod,
               monthlycharges, totalcharges)

    if st.button('Predict'):
        if predict == 1:
            st.warning('The customer will terminate the service.')
        else:
            st.success('The customer is happy with the service.')






if __name__ == '__main__':
    main()
