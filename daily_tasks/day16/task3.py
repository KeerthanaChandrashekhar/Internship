
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# For reproducibility
np.random.seed(42)

# ---------------------------------------------------
# STEP 1: Create heavily skewed dataset
# Example: Income distribution (Right-Skewed)
# ---------------------------------------------------

population_size = 10000

# Exponential distribution → heavily right-skewed
population = np.random.exponential(scale=50000, size=population_size)

# Convert to DataFrame (optional)
data = pd.DataFrame({"Income": population})

# ---------------------------------------------------
# STEP 2: Take 1000 samples of size 30 and compute means
# ---------------------------------------------------

sample_size = 30
num_samples = 1000

sample_means = []

for i in range(num_samples):
    
    # Take random sample
    sample = np.random.choice(population, size=sample_size)
    
    # Calculate mean of sample
    sample_mean = np.mean(sample)
    
    # Store mean
    sample_means.append(sample_mean)

# Convert to Pandas Series
sample_means = pd.Series(sample_means)

# ---------------------------------------------------
# STEP 3: Plot original skewed population
# ---------------------------------------------------

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(population, kde=True)
plt.title("Original Population (Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")

# ---------------------------------------------------
# STEP 4: Plot distribution of sample means
# ---------------------------------------------------

plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (Normal)")
plt.xlabel("Sample Mean Income")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# ---------------------------------------------------
# STEP 5: Compare statistics
# ---------------------------------------------------

print("\nPopulation Mean:", round(np.mean(population), 2))
print("Sample Means Average:", round(np.mean(sample_means), 2))

print("\nPopulation Std Dev:", round(np.std(population), 2))
print("Sample Means Std Dev:", round(np.std(sample_means), 2))

# ---------------------------------------------------
# STEP 6: Explanation
# ---------------------------------------------------

print("\nExplanation:")
print("Original data is heavily skewed.")
print("But distribution of sample means is approximately Normal.")
print("This proves the Central Limit Theorem.")
