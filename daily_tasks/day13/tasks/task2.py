import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('data.csv')

plt.figure()
sns.scatterplot(x="SquareFeet", y="Price", data=df)
plt.title("Square Footage vs House Price")
plt.show()

plt.figure()
sns.boxplot(x= "City", y="Price", data=df)
plt.title("Price distribution based on city")
plt.show()

print("........Insights........")
print("\nPrice increases as the squarefoot increases")