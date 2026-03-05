# CardioRisk AI

CardioRisk AI is a machine learning application that predicts heart disease risk using clinical parameters.

## Features
- Random Forest machine learning model
- FastAPI prediction API
- Streamlit interactive UI
- Probability-based risk prediction

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- Pandas

## How to Run

Install dependencies:

pip install -r requirements.txt

Start API:

uvicorn api.main:app --reload

Start UI:

streamlit run app/app.py