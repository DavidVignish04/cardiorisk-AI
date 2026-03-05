import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import joblib

# Load dataset
df = pd.read_csv("data/HeartDiseaseTrain-Test.csv")

# Convert all text columns to numbers
df = pd.get_dummies(df)

# Target column
y = df["target"]

# Features
X = df.drop("target", axis=1)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Save feature column names
joblib.dump(X.columns, "model_columns.pkl")

# Save trained model
joblib.dump(model, "heart_model.pkl")
print("Model and columns saved successfully")