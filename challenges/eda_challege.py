import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy.stats import skew

data = { 
    "Customer_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], 
    "Gender": 
    ["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female"], 
    "Age": [25,32,28,45,36,23,40,29,31,27], 
    "City_Tier": [1,2,1,3,2,1,3,2,1,2], 
    "Avg_Session_Time": [15,10,18,8,12,20,7,16,14,19],  # in minutes 
    "Pages_Visited": [5,3,6,2,4,8,2,5,6,7], 
    "Products_Viewed": [3,2,4,1,2,5,1,3,4,4], 
    "Previous_Purchases": [2,1,3,0,1,4,0,2,3,3], 
    "Discount_Used": [1,0,1,0,1,1,0,1,1,1],  # 1=Yes, 0=No 
    "Total_Spend": [1200,600,1800,300,900,2500,250,1500,2000,1700] 
} 

df = pd.DataFrame(data) 

print("Task1")
print("\nChecking for null values")
print(df.isnull().sum())

print("\nChecking for duplicates")
print(df.duplicated().sum())

plt.figure(figsize=(15,5))

# Histogram - Total Spend
plt.subplot(1,3,1)
sns.histplot(df['Total_Spend'], kde=True)
plt.title("Total Spend Distribution")
print("Skewness of Total Spend:", skew(df['Total_Spend']))

# Boxplot - Avg Session Time
plt.subplot(1,3,2)
sns.boxplot(x=df['Avg_Session_Time'])
plt.title("Avg Session Time")

# Bar Chart - City Tier
plt.subplot(1,3,3)
sns.countplot(x='City_Tier', data=df)
plt.title("City Tier Distribution")

plt.tight_layout()
plt.show()

print("\n.....Task2.....")
plt.figure(figsize=(15,10))

# Avg Session vs Spend
plt.subplot(2,2,1)
sns.scatterplot(x='Avg_Session_Time', y='Total_Spend', data=df)
plt.title("Session Time vs Total Spend", fontsize = 8)

# Pages Visited vs Spend
plt.subplot(2,2,2)
sns.scatterplot(x='Pages_Visited', y='Total_Spend', data=df)
plt.title("Pages Visited vs Total Spend", fontsize = 8)

# Previous Purchases vs Spend
plt.subplot(2,2,3)
sns.scatterplot(x='Previous_Purchases', y='Total_Spend', data=df)
plt.title("Previous Purchases vs Total Spend", fontsize = 8)

# Discount vs Spend
plt.subplot(2,2,4)
sns.boxplot(x='Discount_Used', y='Total_Spend', data=df)
plt.title("Discount Used vs Total Spend", fontsize = 8)

plt.tight_layout()
plt.show()

print("\n....Tak3....")

plt.figure(figsize=(10,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\n....Task4....")
plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
sns.scatterplot(x='Avg_Session_Time', y='Total_Spend', data=df)
plt.title("Session vs Spend", fontsize = 8)

plt.subplot(2,2,2)
sns.scatterplot(x='Previous_Purchases', y='Total_Spend', data=df)
plt.title("Purchases vs Spend", fontsize = 8)

plt.subplot(2,2,3)
sns.boxplot(x='Discount_Used', y='Total_Spend', data=df)
plt.title("Discount vs Spend", fontsize = 8)

plt.subplot(2,2,4)
sns.histplot(df['Total_Spend'], kde=True)
plt.title("Total Spend", fontsize = 8)

plt.tight_layout()
plt.show()


print()
print("\nCorrelation with Total Spend:")
print(corr['Total_Spend'].sort_values(ascending=False))

