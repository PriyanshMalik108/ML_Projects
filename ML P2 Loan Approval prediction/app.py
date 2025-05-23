import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction App')

no_of_dep = st.slider('choose the number of dependents', 0, 5)
grad = st.selectbox('choose the education', ['Graduate', 'Not Graduate'])
self_emp = st.selectbox('choose the self employed', ['Yes', 'No'])
Annual_income = st.slider('choose the annual income', 0 , 100000000)
loan_amount = st.slider('choose the loan amount', 0 , 100000000)
loan_term = st.slider('choose the loan term', 0 , 20)
Assets = st.slider('choose the assets', 0 , 100000000)
cibil_score = st.slider('choose the cibil score', 0 , 1000)

if grad == 'Graduate':
    grad_s = 0
else:
    grad_s = 1

if self_emp == 'No':
    emp_s = 0
else:
    emp_s = 1

if st.button('Predict'):
    # Preprocess the input data
    pred_data = pd.DataFrame([[	no_of_dep ,	grad_s ,emp_s ,	Annual_income ,	loan_amount ,	loan_term ,	cibil_score ,	Assets ]]
                         , columns=['no_of_dependents' ,	'education' ,	'self_employed' ,	'income_annum' ,	'loan_amount' ,	'loan_term' ,	'cibil_score' ,	'Assets'] )

    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.success('Loan Approved')
    else:
        st.error('Loan Rejected')
