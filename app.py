import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load encoders
cp_encoder = joblib.load("cp_encoder.joblib")
ecg_encoder = joblib.load("ecg_encoder.joblib")

# load model
model = joblib.load("model.joblib")

# read data
data = pd.read_csv("data.csv")

st.title("Heart Health Checker")

# default vals
user_data = {"Age": 0, "Sex": 1, "ChestPainType": "ATA", "Cholesterol": 0, "FastingBS": 0, "RestingECG": "Normal", "MaxHR": 0, "ST_Slope": "Up", "ExerciseAngina": 0, "Oldpeak": 0.0}

# 2 cols
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Patient Age:")
    if age:
        user_data["Age"] = age

    gender = st.radio("Gender:", ["Male", "Female"])
    if gender:
        user_data["Sex"] = 1 if gender == "Male" else 0

    chest_pain = st.selectbox("Chest Pain Type:", data.ChestPainType.unique())
    if chest_pain:
        user_data["ChestPainType"] = chest_pain

    fasting_sugar = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
    if fasting_sugar:
        user_data["FastingBS"] = 1 if fasting_sugar == "Yes" else 0

with col2:
    cholesterol = st.number_input("Cholesterol Level:")
    if cholesterol:
        user_data["Cholesterol"] = cholesterol

    resting_ecg = st.selectbox("Resting ECG Result:", data.RestingECG.unique())
    if resting_ecg:
        user_data["RestingECG"] = resting_ecg

    max_heart_rate = st.number_input("Maximum Heart Rate:")
    if max_heart_rate:
        user_data["MaxHR"] = max_heart_rate

    st_slope = st.selectbox("ST Slope:", data.ST_Slope.unique())
    if st_slope:
        user_data["ST_Slope"] = st_slope

# predict btn
check = st.button("Check Heart Health")
if check:
    # final dict
    final = {
        "Age": user_data["Age"],
        "Sex": user_data["Sex"],
        "ChestPainType": user_data["ChestPainType"],
        "Cholesterol": user_data["Cholesterol"],
        "FastingBS": user_data["FastingBS"],
        "RestingECG": user_data["RestingECG"],
        "MaxHR": user_data["MaxHR"],
        "ExerciseAngina": user_data["ExerciseAngina"],
        "Oldpeak": user_data["Oldpeak"],
        "ST_Slope": user_data["ST_Slope"],
    }

    # make df
    input_df = pd.DataFrame([final])
    st.write(input_df)

    # encode input
    input_df["ChestPainType"] = cp_encoder.transform(input_df["ChestPainType"])
    input_df["RestingECG"] = ecg_encoder.transform(input_df["RestingECG"])
    input_df["ST_Slope"] = input_df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})

    # predict
    result = model.predict(input_df)
    output = "Heart Disease Detected" if result[0] == 1 else "No Heart Disease"
    st.success(f"Result: {output}")
