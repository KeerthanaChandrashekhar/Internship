import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv("data.csv")

corr_matrix = df[["Price", "Bedrooms", "SquareFeet"]].corr()


plt.figure()
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Matrix")
plt.show()

print("\nHighly Correlated Features (> 0.8):\n")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} → {corr_matrix.iloc[i, j]:.2f}")

plt.figure(figsize=(6,4))
sns.boxplot(x=df["Price"])
plt.title("Price Boxplot")
plt.show()

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower) | (df["Price"] > upper)]

print("\nOutlier Houses:\n")
print(outliers)
