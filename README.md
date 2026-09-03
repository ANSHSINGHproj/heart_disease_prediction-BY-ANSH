# heart_disease_prediction-BY-ANSH
heart-disease-prediction

# heart_disease_prediction-BY-ANSH

heart-disease-prediction

This is a simple app I made to check heart disease risk.

You give some basic info like age, gender, chest pain type, cholesterol, ECG result, max heart rate, ST slope etc. and it tells you if there is risk of heart disease or not.
I used a Random Forest model for this, trained on a heart disease dataset (around 918 patients).

Live app link: https://heartdiseaseprediction-by-ansh-cnyvknwp7er9bm3rvir5p5.streamlit.app/

-Files in this project-

- app.py - main streamlit app code
- requirements.txt - libraries needed to run the app
- model.joblib - trained model
- cp_encoder.joblib - encoder for chest pain type
- ecg_encoder.joblib - encoder for resting ECG
- data.csv - original dataset
- final_data.csv - cleaned dataset
- index.ipynb - notebook where I trained the model
- index.txt - some basic analysis notes of the data
