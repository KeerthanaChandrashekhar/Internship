import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy.stats import skew, kurtosis 

df = pd.read_csv('data.csv')

plt.figure()
sns.histplot(df['Price'], kde=True)
plt.title("Housing Price Distribution")
plt.show()

print("Skewness:", skew(df['Price']))
print("kurtosis:", kurtosis(df['Price']))

plt.figure()
sns.countplot(x="City", data=df)
plt.title("Number of Houses per city")
plt.show()
