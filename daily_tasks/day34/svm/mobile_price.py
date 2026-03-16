# Mobile Price Classification - SVM C Parameter Test

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("iabhishekofficial/mobile-price-classification")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "train.csv"))

# Features and target
X = df.drop("price_range", axis=1)
y = df["price_range"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Test different C values
C_values = [0.01, 0.1, 1, 10, 100]

for c in C_values:
    model = SVC(C=c, kernel="linear")
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    print(f"C = {c} → Accuracy: {acc}")