# Credit Card Fraud Detection

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "creditcard.csv"))

# Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nFraud Detection Report:\n")
print(classification_report(y_test, pred))