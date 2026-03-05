from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model and column structure
model = joblib.load("heart_model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.get("/")
def home():
    return {"message": "CardioRisk AI API Running"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    # Encode categorical features
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
    "heart_disease_risk": int(prediction),
    "risk_probability": float(probability)
    }

