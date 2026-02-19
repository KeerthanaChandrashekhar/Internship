# zscore_outliers.py

# Import libraries
import pandas as pd
import numpy as np

# -----------------------------------------
# STEP 1: Create or Load Dataset
# -----------------------------------------

# Example dataset (you can replace this with CSV loading)
np.random.seed(42)

data = pd.DataFrame({
    "Student_ID": range(1, 21),
    "Score": np.random.normal(loc=70, scale=10, size=20)
})

# Add extreme values (outliers)
data.loc[18, "Score"] = 120
data.loc[19, "Score"] = 20

print("Original Data:\n")
print(data)


# -----------------------------------------
# STEP 2: Calculate Mean and Standard Deviation
# -----------------------------------------

mean_value = data["Score"].mean()
std_value = data["Score"].std()

print("\nMean (μ):", round(mean_value, 2))
print("Standard Deviation (σ):", round(std_value, 2))


# -----------------------------------------
# STEP 3: Calculate Z-Score
# Formula: Z = (x - μ) / σ
# -----------------------------------------

data["z_score"] = (data["Score"] - mean_value) / std_value

print("\nData with Z-score:\n")
print(data)


# -----------------------------------------
# STEP 4: Identify Outliers (|Z| > 3)
# -----------------------------------------

outliers = data[abs(data["z_score"]) > 3]

print("\nOutliers (|Z| > 3):\n")

if len(outliers) == 0:
    print("No outliers found.")
else:
    print(outliers)


# -----------------------------------------
# STEP 5: Explanation print
# -----------------------------------------

print("\nExplanation:")
print("Z-score tells how many standard deviations a value is from the mean.")
print("Z = 0 → exactly average")
print("Z = 2 → above average")
print("Z = -2 → below average")
print("|Z| > 3 → Extreme value (Outlier)")
