import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(style = "whitegrid")

data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Department": ["IT","HR"," IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F"]
}

df = pd.DataFrame(data)
print(df)

plt.figure()
sns.scatterplot(x= "Age", y="Salary", data= df)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.boxplot(x= "Gender", y= "Salary", data=df)
plt.title("Salary by Gender")
plt.show()

plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by department")
plt.show()

corr_matrix = df.corr(numeric_only= True)
print("\nCorrelation Matrix")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="PuBu_r")
plt.title("Correlation Heatmap")
plt.show()

plt.figure()
sns.boxplot(x= df["Age"])
plt.title("Age Outliers")
plt.show()

plt.figure()
sns.boxplot(x= df["Experience"])
plt.title("Experience Outliers")
plt.show()


#FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.


print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")