# Pulsar Star Prediction using SVM

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("colearninglounge/predicting-pulsar-starintermediate")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "pulsar_data_train.csv"))

# Remove missing values
df = df.dropna()

# Features and target
X = df.drop("target_class", axis=1)
y = df["target_class"]

# Create train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train SVM model
model = SVC(kernel="rbf", class_weight="balanced")

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))