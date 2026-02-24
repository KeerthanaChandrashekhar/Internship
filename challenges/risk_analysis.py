import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

data = pd.read_csv("manufacturing_quality_dataset.csv")

#target_weight = 50
#underweight_limit = 47

#1.Are weights normally distributed?

mean = data['Weight'].mean()
median = data['Weight'].median()
std = data['Weight'].std()
#skew = data['Weight'].skew()

print("=== NORMAL DISTRIBUTION CHECK ===")
print("Mean:", round(mean,2))
print("Median:", round(median,2))
print("Standard Deviation:", round(std,2))
#print("Skewness:", round(skew,2))

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


#2.Probability Using Normal Distribution

given_mean = 100
given_std = 5

#P(weight < 90g)
z_90 = (90 - given_mean)/given_std
p_90 = norm.cdf(z_90)

print("Z_score for value 90:", round(z_90,2))
print("\nP(weight < 90g):", round(p_90,4))

# P(95 < weight < 105)
z_95 = (95 - given_mean)/given_std
z_105 = (105 - given_mean)/given_std
p_value = norm.cdf(z_105) - norm.cdf(z_95)

print("\nZ_score for value 95:", round(z_95,2))
print("\nZ_score for value 105:", round(z_105,2))
print("\nP(95 < weight < 105)", round(p_value,4))

#3.Central Limit Theorem Application

sample_means = []

batches = data['Batch_id'].unique()

for batch in batches:

    batch_data = data[data['Batch_id'] == batch]['Weight']

    if len(batch_data) >= 40:

        sample = batch_data.sample(40)

        sample_means.append(sample.mean())

sample_means = np.array(sample_means)

print("\nNumber of samples:", len(sample_means))
print("\nMean of sample means:", round(sample_means.mean(),2))
print("\nStd of sample means:", round(sample_means.std(),2))

plt.figure(figsize=(10,6))

sns.histplot(sample_means, bins=20, kde=True)

plt.title("Sampling Distribution of Sample Means (CLT)")
plt.show()

print("ConclusioN: Sampling distribution is approximately normal")

#print(data.columns)

#4.Process Control Using Z-score

data['z_score'] = (data['Weight'] - mean)/ std

defective_parts = data[abs(data['Weight']) > 2.5]

print("\nTotal parts:", len(data))
print("\nDefective parts:", len(defective_parts))

print("\nDefective parts sample:")
print(defective_parts[['Batch_id','Part_id','Weight','z_score']].head())

#Defective Batch Detection

print("\nDefective Batch Detection")

defective_batches = defective_parts['Batch_id'].unique()

print("\nNumber of defective batches:", len(defective_batches))
print("Defective batch IDs:", defective_batches)


print("\nPROCESS STABILITY CHECK")

UCL = mean + 3*std
LCL = mean - 3*std

print("UCL:", round(UCL,2))
print("LCL:", round(LCL,2))

out_of_control = data[(data['Weight'] > UCL) | (data['Weight'] < LCL)]

print("Out-of-control parts:", len(out_of_control))

if len(out_of_control) == 0:
    print("Process is STABLE")
else:
    print("Process needs investigation")


# Control chart
plt.figure(figsize=(12,6))

plt.plot(data['Weight'], marker='o', linestyle='-', markersize=3)

plt.axhline(mean, color='green', label='Mean')
plt.axhline(UCL, color='red', linestyle='--', label='UCL')
plt.axhline(LCL, color='red', linestyle='--', label='LCL')

plt.title("Process Control Chart")
plt.legend()
plt.show()



print("\nFINAL SUMMARY")

print("Normally Distributed:",
      "YES" if abs(mean - median) < 0.1 else "NO")

print("Defective batches:", len(defective_batches))

probability_defective = len(defective_parts) / len(data)

print("Probability of defective part:",
      round(probability_defective*100,2), "%")

print("Process Stability:",
      "STABLE" if len(out_of_control)==0 else "UNSTABLE")
