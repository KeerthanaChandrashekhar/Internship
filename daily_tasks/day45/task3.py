import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Download dataset
path = kagglehub.dataset_download("yasserh/wine-quality-dataset")

print("Dataset path:", path)
print("Files:", os.listdir(path))


# Load dataset
df = pd.read_csv(os.path.join(path, "WineQT.csv"))

print(df.head())


# Features and Target
X = df.drop(["quality", "Id"], axis=1)
y = df["quality"]


# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA (11 → 2 components)
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

print("\nExplained Variance:", pca.explained_variance_ratio_)


# Scatter Plot
plt.figure(figsize=(6,5))

scatter = plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=y
)

plt.title("PCA Visualization of Wine Quality")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.colorbar(scatter, label="Wine Quality")

plt.show()                 