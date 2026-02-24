# skewness_analysis.py

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

# For reproducibility (same random data every run)
np.random.seed(42)

# ---------------------------------------
# STEP 1: Generate datasets
# ---------------------------------------

# Normal Distribution → Human Heights
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution → Household Incomes
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution → Easy Exam Scores
scores = 100 - np.random.exponential(scale=10, size=1000)

# Create Pandas DataFrame
data = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

# ---------------------------------------
# STEP 2: Plot Histogram with KDE
# ---------------------------------------

plt.figure(figsize=(15, 5))

# Normal Distribution Plot
plt.subplot(1, 3, 1)
sns.histplot(data["Heights"], kde=True)
plt.title("Normal Distribution (Heights)")
plt.xlabel("Height")
plt.ylabel("Frequency")

# Right-Skewed Plot
plt.subplot(1, 3, 2)
sns.histplot(data["Incomes"], kde=True)
plt.title("Right-Skewed Distribution (Incomes)")
plt.xlabel("Income")
plt.ylabel("Frequency")

# Left-Skewed Plot
plt.subplot(1, 3, 3)
sns.histplot(data["Scores"], kde=True)
plt.title("Left-Skewed Distribution (Scores)")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# ---------------------------------------
# STEP 3: Compare Mean and Median
# ---------------------------------------

print("\n--- Mean vs Median Comparison ---\n")

for column in data.columns:
    
    mean_value = data[column].mean()
    median_value = data[column].median()
    skew_value = data[column].skew()
    
    print(f"{column}:")
    print(f"Mean   = {mean_value:.2f}")
    print(f"Median = {median_value:.2f}")
    print(f"Skew   = {skew_value:.2f}")
    
    # Determine skew type
    if mean_value > median_value:
        print("Distribution Type: Right-Skewed")
    elif mean_value < median_value:
        print("Distribution Type: Left-Skewed")
    else:
        print("Distribution Type: Normal Distribution")
    
    print("-----------------------------")
