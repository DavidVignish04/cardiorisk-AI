import streamlit as st
import requests

st.title("CardioRisk AI")
st.subheader("Heart Disease Risk Prediction")
st.write("AI-based Heart Disease Risk Prediction System")

# -------------------------
# User Inputs
# -------------------------

age = st.number_input("Age", 20, 100, 50)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

chest_pain_type = st.selectbox(
    "Chest Pain Type",
    [
        "Typical angina",
        "Atypical angina",
        "Non-anginal pain",
        "Asymptomatic"
    ]
)

resting_blood_pressure = st.number_input(
    "Resting Blood Pressure",
    80, 200, 120
)

cholesterol = st.number_input(
    "Cholesterol",
    100, 600, 200
)

fasting_blood_sugar = st.selectbox(
    "Fasting Blood Sugar",
    [
        "Lower than 120 mg/ml",
        "Greater than 120 mg/ml"
    ]
)

rest_ecg = st.selectbox(
    "Rest ECG Result",
    [
        "Normal",
        "ST-T wave abnormal",
        "Left ventricular hypertrophy"
    ]
)

max_heart_rate = st.number_input(
    "Max Heart Rate Achieved",
    60, 220, 150
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["Yes", "No"]
)

oldpeak = st.number_input(
    "Oldpeak (ST Depression)",
    0.0, 6.0, 1.0
)

slope = st.selectbox(
    "Slope of ST Segment",
    ["Upsloping", "Flat", "Downsloping"]
)

vessels = st.selectbox(
    "Number of Major Vessels Colored",
    ["Zero", "One", "Two", "Three"]
)

thalassemia = st.selectbox(
    "Thalassemia",
    ["Normal", "Fixed Defect", "Reversible Defect"]
)

# -------------------------
# Prediction Button
# -------------------------

if st.button("Predict Risk"):

    patient_data = {
        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_blood_pressure": resting_blood_pressure,
        "cholesterol": cholesterol,
        "fasting_blood_sugar": fasting_blood_sugar,
        "rest_ecg": rest_ecg,
        "Max_heart_rate": max_heart_rate,
        "exercise_induced_angina": exercise_angina,
        "oldpeak": oldpeak,
        "slope": slope,
        "vessals_colored_by": vessels,
        "thalassemia": thalassemia
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=patient_data
        )

        result = response.json()

        risk = result["heart_disease_risk"]
        probability = result.get("risk_probability", None)

        st.subheader("Prediction Result")

        if risk == 1:
            st.error("High Risk of Heart Disease")
        else:
            st.success("Low Risk of Heart Disease")

        if probability is not None:
            prob_percent = round(probability * 100, 2)
            st.write(f"Risk Probability: {prob_percent}%")

            if probability < 0.3:
                st.success("Risk Category: Low")
            elif probability < 0.6:
                st.warning("Risk Category: Moderate")
            else:
                st.error("Risk Category: High")

    except Exception as e:
        st.error("Error connecting to prediction API")
        st.write(e)