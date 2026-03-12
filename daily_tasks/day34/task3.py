# Social Media Ads - Feature Importance

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import os
import kagglehub

# Download dataset
path = kagglehub.dataset_download("rakeshrau/social-network-ads")

print("Dataset path:", path)
print("Files:", os.listdir(path))

# Load dataset
df = pd.read_csv(os.path.join(path, "Social_Network_Ads.csv"))

# Drop unnecessary column
df.drop("User ID", axis=1, inplace=True)

# Convert Gender to numeric
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# Features and target
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Feature importance
importance = model.feature_importances_
features = X.columns

# Plot
plt.barh(features, importance)
plt.xlabel("Importance")
plt.title("Feature Importance in Ad Purchase Prediction")
plt.show()