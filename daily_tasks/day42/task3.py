import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import kagglehub
import os

# Download dataset
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "StudentsPerformance.csv"))

print(df.head())

# Select numerical score columns
X = df[["math score", "reading score", "writing score"]]

# -----------------------------
# Elbow Method
# -----------------------------
wcss = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    wcss.append(model.inertia_)

# Plot elbow graph
plt.figure(figsize=(6,4))
plt.plot(range(1,11), wcss, marker="o")

plt.title("Elbow Method for Student Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")

plt.show()

# -----------------------------
# Train final K-Means model
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42)

clusters = kmeans.fit_predict(X)

# Add cluster labels to dataframe
df["Cluster"] = clusters

# -----------------------------
# Visualize clusters
# -----------------------------
plt.figure(figsize=(6,4))

plt.scatter(
    df["math score"],
    df["reading score"],
    c=df["Cluster"]
)

# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=200,
    c="red",
    marker="X"
)

plt.title("Student Performance Clusters")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")

plt.show()

# -----------------------------
# Print centroid values
# -----------------------------
centroids = pd.DataFrame(
    kmeans.cluster_centers_,
    columns=["Math Avg", "Reading Avg", "Writing Avg"]
)

print("\nCentroids (Average Scores of Each Cluster):")
print(centroids)  