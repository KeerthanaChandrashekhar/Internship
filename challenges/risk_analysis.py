import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

data = pd.read_csv("manufacturing_quality_dataset.csv")

target_weight = 50
underweight_limit = 47

#1.Are weights normally distributed?

mean = data['Weight'].mean()
median = data['Weight'].median()
std = data['Weight'].std()
skew = data['Weight'].skew()

print("=== NORMAL DISTRIBUTION CHECK ===")
print("Mean:", round(mean,2))
print("Median:", round(median,2))
print("Standard Deviation:", round(std,2))
print("Skewness:", round(skew,2))

if abs(mean - median) < 0.1:
    print("Conclusion: Distribution is approximately NORMAL\n")
else:
    print("Conclusion: Distribution is SKEWED\n")


# Plot histogram with normal curve
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))

sns.histplot(data['Weight'], bins=30, stat='density', alpha=0.5, label='Histogram')

x = np.linspace(data['Weight'].min(), data['Weight'].max(), 100)
normal_curve = norm.pdf(x, mean, std)

plt.plot(x, normal_curve, color='red', linewidth=3, label='Normal Curve')

plt.axvline(mean, color='green', linestyle='-', linewidth=3, label=f'Mean = {mean:.2f}')
plt.axvline(median, color='blue', linestyle='--', linewidth=3, label=f'Median = {median:.2f}')

plt.title("Weight Distribution vs Normal Curve")
plt.xlabel("Weight")
plt.ylabel("Density")
plt.legend()
plt.show()


#2.Are there defective batches?

defective = data[data['Weight'] < underweight_limit]

print("=== DEFECTIVE PART ANALYSIS ===")
print("Total parts:", len(data))
print("Defective parts:", len(defective))

defective_batches = defective['Batch_id'].unique()

print("Number of defective batches:", len(defective_batches))
print("Defective batch IDs:", defective_batches, "\n")


# Batch defect rate
batch_defect_rate = data.groupby('Batch_id')['Weight'].apply(
    lambda x: (x < underweight_limit).mean()
)

print("Top 5 worst batches:")
print(batch_defect_rate.sort_values(ascending=False).head(), "\n")


#3.Probability of underweight product

probability = len(defective) / len(data)

print("=== PROBABILITY ANALYSIS ===")
print("Probability of underweight product:", round(probability,4))
print("Percentage:", round(probability*100,2), "%\n")


# QUESTION 4: Is the process stable? (Control Chart)

UCL = mean + 3*std
LCL = mean - 3*std

print("=== PROCESS STABILITY ANALYSIS ===")
print("Mean:", round(mean,2))
print("Upper Control Limit (UCL):", round(UCL,2))
print("Lower Control Limit (LCL):", round(LCL,2))

out_of_control = data[(data['Weight'] > UCL) | (data['Weight'] < LCL)]

print("Out-of-control parts:", len(out_of_control))

if len(out_of_control) == 0:
    print("Conclusion: Process is STABLE\n")
else:
    print("Conclusion: Process is NOT fully stable\n")


# Control Chart
plt.figure(figsize=(12,6))

plt.plot(data['Weight'], marker='o', linestyle='-', markersize=3)

plt.axhline(mean, color='green', linewidth=2, label='Mean')
plt.axhline(UCL, color='red', linestyle='--', linewidth=2, label='UCL')
plt.axhline(LCL, color='red', linestyle='--', linewidth=2, label='LCL')

plt.title("Process Control Chart")
plt.xlabel("Part Index")
plt.ylabel("Weight")
plt.legend()
plt.show()



#FINAL SUMMARY

print("=== FINAL MANAGEMENT SUMMARY ===")

print("1. Normal Distribution:",
      "YES" if abs(mean - median) < 0.1 else "NO")

print("2. Defective batches found:", len(defective_batches))

print("3. Underweight probability:", str(round(probability*100,2)) + "%")

print("4. Process stability:", "STABLE" if len(out_of_control) == 0 else "UNSTABLE")