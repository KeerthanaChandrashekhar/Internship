import pandas as pd
import os
import time
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Download Dataset
path = kagglehub.dataset_download("datamunge/sign-language-mnist")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load Dataset
df = pd.read_csv(os.path.join(path, "sign_mnist_train.csv"))

print(df.head())


# Features and Target
X = df.drop("label", axis=1)
y = df["label"]


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model 1: Train on Raw Data (784 Pixels)
model_raw = LogisticRegression(max_iter=1000)

start_time = time.time()

model_raw.fit(X_train, y_train)

raw_train_time = time.time() - start_time

# Predictions
pred_raw = model_raw.predict(X_test)

# Accuracy
raw_accuracy = accuracy_score(y_test, pred_raw)

print("\nRaw Data Model")
print("Training Time:", raw_train_time)
print("Accuracy:", raw_accuracy)


# Apply PCA (Reduce 784 → 50 Components)
pca = PCA(n_components=50)

X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)


# Model 2: Train on PCA Data
model_pca = LogisticRegression(max_iter=1000)

start_time = time.time()

model_pca.fit(X_train_pca, y_train)

pca_train_time = time.time() - start_time

# Predictions
pred_pca = model_pca.predict(X_test_pca)

# Accuracy
pca_accuracy = accuracy_score(y_test, pred_pca)

print("\nPCA Model")
print("Training Time:", pca_train_time)
print("Accuracy:", pca_accuracy)

# Speedup Factor
speedup = raw_train_time / pca_train_time

print("\nSpeedup Factor:", speedup)