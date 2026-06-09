import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📊 Customer Churn Prediction")

# Load model
model = joblib.load("models/churn_model.pkl")

st.header("Customer Details")

tenure = st.number_input("Tenure", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", value=50.0)

if st.button("Predict Churn"):

    sample = pd.DataFrame({
        'gender': [1],
        'SeniorCitizen': [0],
        'Partner': [1],
        'Dependents': [0],
        'tenure': [tenure],
        'PhoneService': [1],
        'MultipleLines': [1],
        'InternetService': [1],
        'OnlineSecurity': [0],
        'OnlineBackup': [1],
        'DeviceProtection': [0],
        'TechSupport': [0],
        'StreamingTV': [1],
        'StreamingMovies': [1],
        'Contract': [0],
        'PaperlessBilling': [1],
        'PaymentMethod': [2],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [tenure * monthly_charges]
    })

    prediction = model.predict(sample)
    probability = model.predict_proba(sample)

    st.write(f"Churn Probability: {probability[0][1] * 100:.2f}%")

    if prediction[0] == 1:
        st.success("✅ Customer will stay")
else:
    st.error("⚠ Customer may churn")