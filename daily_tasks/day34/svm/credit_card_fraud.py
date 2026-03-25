# Credit Card Fraud Detection using SVM

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
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

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# SVM Model (Linear - faster)
model = LinearSVC(class_weight='balanced', max_iter=5000)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

print("\nFraud Detection Report (SVM):\n")
print(classification_report(y_test, pred))