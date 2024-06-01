# -*- coding: utf-8 -*-
"""medical_insurance_cost_predictor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10dSZqICwMNSSkYmuUw4s3bjFIksIJVeJ
"""

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('medical_insurance_cost.pkl')

# Title of the app
st.title("Medical Insurance Cost Prediction - USA")

# Inputs for the user
age = st.number_input("Age", min_value=0, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=30.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=2)
sex_male = st.selectbox("Sex", ["Male", "Female"])
smoker_yes = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Convert categorical inputs to numerical
sex_male = 1 if sex_male == "Male" else 0
smoker_yes = 1 if smoker_yes == "Yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'sex_male': [sex_male],
    'smoker_yes': [smoker_yes],
    'region_northwest': [region_northwest],
    'region_southeast': [region_southeast],
    'region_southwest': [region_southwest],
    'age_bmi_interaction': [age * bmi]
})

# Predict the charges
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Charges: ${prediction[0]:.2f}")
