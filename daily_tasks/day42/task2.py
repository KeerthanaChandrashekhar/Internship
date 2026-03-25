import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("arjunbhasin2013/ccdata")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "CC GENERAL.csv"))

print(df.head())

# Select required columns
X = df[["PURCHASES", "PURCHASES_FREQUENCY"]]

# Remove missing values
X = X.dropna()

# ----------------------------
# STEP A: K-Means without scaling
# ----------------------------
kmeans_unscaled = KMeans(n_clusters=3, random_state=42)

clusters_unscaled = kmeans_unscaled.fit_predict(X)

plt.figure(figsize=(6,4))
plt.scatter(
    X["PURCHASES"],
    X["PURCHASES_FREQUENCY"],
    c=clusters_unscaled
)

plt.title("K-Means without Scaling")
plt.xlabel("PURCHASES")
plt.ylabel("PURCHASES_FREQUENCY")

plt.show()

# ----------------------------
# STEP B: Apply StandardScaler
# ----------------------------
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Run K-Means again
kmeans_scaled = KMeans(n_clusters=3, random_state=42)

clusters_scaled = kmeans_scaled.fit_predict(X_scaled)

plt.figure(figsize=(6,4))
plt.scatter(
    X_scaled[:,0],
    X_scaled[:,1],
    c=clusters_scaled
)

plt.title("K-Means with StandardScaler")
plt.xlabel("Scaled PURCHASES")
plt.ylabel("Scaled PURCHASES_FREQUENCY")

plt.show()