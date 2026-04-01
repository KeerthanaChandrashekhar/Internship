import pandas as pd
import numpy as np
import os
import time
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


# ===============================
# STEP 1: Download Dataset (KaggleHub)
# ===============================

path = kagglehub.dataset_download("benroshan/factors-affecting-campus-placement")

print("Dataset path:", path)
print("Files:", os.listdir(path))


# ===============================
# STEP 2: Load Dataset
# ===============================

df = pd.read_csv(os.path.join(path, "Placement_Data_Full_Class.csv"))

print("\nDataset Preview:")
print(df.head())


# ===============================
# STEP 3: Data Preprocessing
# ===============================

# Drop unnecessary columns
df = df.drop(['sl_no','salary'], axis=1)

# Encode categorical columns
le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])


# Features and Target
X = df.drop("status", axis=1)
y = df["status"]


# ===============================
# STEP 4: Train Test Split (80/20)
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ===============================
# STEP 5: Feature Scaling
# ===============================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)   # fit only on train
X_test = scaler.transform(X_test)         # transform test


# ===============================
# STEP 6: Baseline Random Forest
# ===============================

print("\nTraining Baseline Model")

baseline_model = RandomForestClassifier(random_state=42)

baseline_model.fit(X_train, y_train)

y_pred = baseline_model.predict(X_test)

baseline_accuracy = accuracy_score(y_test, y_pred)
baseline_f1 = f1_score(y_test, y_pred)

print("Baseline Accuracy:", baseline_accuracy)
print("Baseline F1 Score:", baseline_f1)


# ===============================
# STEP 7: Grid Search Parameters
# ===============================

param_grid = {
    "n_estimators": [50,100,200],
    "max_depth": [None,10,20],
    "min_samples_split": [2,5,10]
}


# ===============================
# STEP 8: Grid Search (Accuracy)
# ===============================

print("\nRunning GridSearchCV (Accuracy)")

grid_acc = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_acc.fit(X_train, y_train)

print("Best Params (Accuracy):", grid_acc.best_params_)


# ===============================
# STEP 9: Grid Search (F1 Score)
# ===============================

print("\nRunning GridSearchCV (F1)")

grid_f1 = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="f1"
)

grid_f1.fit(X_train, y_train)

print("Best Params (F1):", grid_f1.best_params_)


# ===============================
# STEP 10: Measure GridSearch Time
# ===============================

start = time.time()

grid_f1.fit(X_train, y_train)

grid_time = time.time() - start

best_grid_f1 = grid_f1.best_score_

print("\nGridSearch Time:", grid_time)
print("Best Grid F1:", best_grid_f1)


# ===============================
# STEP 11: Randomized Search
# ===============================

param_dist = {
    "n_estimators": np.arange(10,500),
    "max_depth": [None,10,20,30,40],
    "min_samples_split": np.arange(2,20)
}

print("\nRunning RandomizedSearchCV")

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=20,
    cv=5,
    scoring="f1",
    random_state=42
)

start = time.time()

random_search.fit(X_train, y_train)

random_time = time.time() - start

best_random_f1 = random_search.best_score_

print("Random Search Time:", random_time)
print("Best Random F1:", best_random_f1)


# ===============================
# STEP 12: Final Comparison
# ===============================

print("\n========= Comparison =========")

results = pd.DataFrame({
    "Method": ["GridSearchCV","RandomizedSearchCV"],
    "Time Taken": [grid_time, random_time],
    "Best F1 Score": [best_grid_f1, best_random_f1]
})

print(results)