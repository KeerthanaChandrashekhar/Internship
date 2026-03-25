import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download(
    "vjchoudhary7/customer-segmentation-tutorial-in-python"
)

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "Mall_Customers.csv"))

# Show first few rows
print(df.head())

# Select features for clustering
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# -------------------------
# Elbow Method
# -------------------------
wcss = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    wcss.append(model.inertia_)

# Plot Elbow graph
plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# -------------------------
# Train Final Model
# -------------------------
kmeans = KMeans(n_clusters=5, random_state=42)

clusters = kmeans.fit_predict(X)

# -------------------------
# Visualize Clusters
# -------------------------
plt.scatter(
    X["Annual Income (k$)"],
    X["Spending Score (1-100)"],
    c=clusters
)

# Cluster centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    c="red",
    marker="X"
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.show()