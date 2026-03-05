# CardioRisk AI

CardioRisk AI is a machine learning application that predicts the risk of heart disease using patient clinical data.
The system uses a Random Forest model trained on a heart disease dataset and provides predictions through a FastAPI backend with a Streamlit user interface.

## Features

* Heart disease risk prediction using machine learning
* Random Forest classifier trained on clinical dataset
* FastAPI backend for model inference
* Streamlit UI for interactive prediction
* Probability-based risk output

## Tech Stack

* Python
* Scikit-learn
* Pandas
* FastAPI
* Streamlit
* Joblib

## Project Structure

cardiorisk-ai/

api/
 main.py – FastAPI server for predictions

app/
 app.py – Streamlit user interface

data/
 HeartDiseaseTrain-Test.csv – dataset

models/
 heart_model.pkl – trained model
 model_columns.pkl – feature columns

train.py – model training script
requirements.txt – dependencies

## Installation

Clone the repository:

git clone https://github.com/DavidVignish04/cardiorisk-ai.git

Go to the project directory:

cd cardiorisk-ai

Install dependencies:

pip install -r requirements.txt

## Run the Application

Start the API server:

uvicorn api.main:app --reload

Start the Streamlit interface:

streamlit run app/app.py

The UI will open in your browser where you can enter patient data and get a heart disease risk prediction.


