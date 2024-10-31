import streamlit as st
import numpy as np
import pickle

# Load the saved heart disease prediction model
model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Streamlit app
st.title('Heart Disease Prediction System')

# Collect user input for model features
age = st.number_input('Age', min_value=1, max_value=120)
sex = st.selectbox('Sex (0: Female, 1: Male)', [0, 1])
cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200)
chol = st.number_input('Cholesterol Level', min_value=100, max_value=400)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1: Yes, 0: No)', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results (0-2)', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220)
exang = st.selectbox('Exercise Induced Angina (1: Yes, 0: No)', [0, 1])
oldpeak = st.number_input('ST Depression Induced by Exercise')
slope = st.selectbox('Slope of the Peak Exercise ST Segment (0-2)', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels (0-4)', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia (0-3)', [0, 1, 2, 3])

# Prepare input data for prediction
input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
input_data = np.asarray(input_data).reshape(1, -1)

# Predict and display result
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("The model predicts the presence of heart disease.")
    else:
        st.success("The model predicts no presence of heart disease.")
