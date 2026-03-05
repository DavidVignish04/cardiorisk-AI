import joblib
import pandas as pd

# Load model and column structure
model = joblib.load("heart_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Example patient data
patient = {
    "age": 55,
    "sex": "Male",
    "chest_pain_type": "Typical angina",
    "resting_blood_pressure": 140,
    "cholesterol": 240
}

# Convert to dataframe
df = pd.DataFrame([patient])

# Apply same encoding as training
df = pd.get_dummies(df)

# Ensure same columns as training
df = df.reindex(columns=model_columns, fill_value=0)

# Predict
prediction = model.predict(df)

print("Heart Disease Prediction:", prediction)