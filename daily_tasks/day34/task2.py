# Wine Quality - Scaling Experiment

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("yasserh/wine-quality-dataset")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "WineQT.csv"))

# Features and target
X = df.drop(["quality", "Id"], axis=1)
y = df["quality"]

# Convert to binary classification (good vs bad wine)
y = (y >= 6).astype(int)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model without scaling
model1 = LogisticRegression(max_iter=2000)
model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)
print("\nAccuracy WITHOUT scaling:", accuracy_score(y_test, pred1))

# Apply scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model with scaling
model2 = LogisticRegression(max_iter=2000)
model2.fit(X_train_scaled, y_train)

pred2 = model2.predict(X_test_scaled)
print("Accuracy WITH scaling:", accuracy_score(y_test, pred2))