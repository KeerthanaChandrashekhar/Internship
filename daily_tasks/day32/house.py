import kagglehub
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Download dataset
path = kagglehub.dataset_download("harlfoxem/housesalesprediction")
print("Path to dataset files:", path)

# Read CSV
csv_path = os.path.join(path, "kc_house_data.csv")
df = pd.read_csv(csv_path)

print(df.head())

# Features and target
X = df[['bedrooms', 'bathrooms', 'sqft_living']]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeRegressor(max_depth=3, min_samples_split=5, min_samples_leaf=2)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)
print(predictions[:5])

# Plot decision tree
plt.figure(figsize=(15,8))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()