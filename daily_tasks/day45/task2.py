import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# -----------------------------
# Download dataset
# -----------------------------
path = kagglehub.dataset_download(
    "vjchoudhary7/customer-segmentation-tutorial-in-python"
)

print("Dataset path:", path)
print("Files:", os.listdir(path))

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(os.path.join(path, "Mall_Customers.csv"))

print(df.head())

# -----------------------------
# Select numerical columns
# -----------------------------
X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# -----------------------------
# Standardize the data
# -----------------------------
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# -----------------------------
# Run PCA (no fixed components)
# -----------------------------
pca = PCA()

pca.fit(X_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()

# -----------------------------
# Plot Scree / Cumulative Variance
# -----------------------------
plt.figure(figsize=(6,4))

plt.plot(
    range(1, len(cumulative_variance)+1),
    cumulative_variance,
    marker="o"
)

plt.axhline(y=0.95, linestyle="--")

plt.title("Cumulative Explained Variance (PCA)")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Variance")

plt.show()

# -----------------------------
# Find number of components for 95%
# -----------------------------
components_95 = (cumulative_variance >= 0.95).argmax() + 1

print("\nComponents needed to retain 95% variance:", components_95)