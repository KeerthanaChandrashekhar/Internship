import pandas as pd
import os
import kagglehub

from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Download dataset
path = kagglehub.dataset_download("muratkokludataset/pumpkin-seeds-dataset")

print("Dataset path:", path)
print("Files in dataset:", os.listdir(path))

# Load ARFF file
data = arff.loadarff(os.path.join(path, "Pumpkin_Seeds_Dataset", "Pumpkin_Seeds_Dataset.arff"))
df = pd.DataFrame(data[0])

# Convert bytes to string
df["Class"] = df["Class"].str.decode("utf-8").str.strip()

# Encode labels automatically
le = LabelEncoder()
df["Class"] = le.fit_transform(df["Class"])

print(df.head())
print(df.info())

# Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred)) 