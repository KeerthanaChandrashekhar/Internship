import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["anita", "RAHUL", "meena", "Arjun"],
    "Math": [45, 78, np.nan, 35],
    "Science": [50, 82, 30, np.nan],
    "English": [55, 75, 25, 40],
    "Attendance": [70, 90, 60, 72],
    "Study_Hours": [8, 15, 5, 6],
    "Parent_Edu": ["Below High School", "Graduate",
                   "Below High School", "High School"],
    "Result": ["Fail", "Pass", "Fail", "Fail"]
})

print(df.isnull().sum())

df[["Math","Science","English"]] = df[["Math","Science","English"]].fillna(df.mean(numeric_only=True))

df["Name"] = df["Name"].str.title()
print(df.isnull().sum())

df["Avg"] = df[["Math","Science","English"]].mean(axis=1)

df["Risk_Score"] = (
    (df["Avg"] < 50).astype(int) * 40 +
    (df["Attendance"] < 75).astype(int) * 30 +
    (df["Study_Hours"] < 10).astype(int) * 20 +
    (df["Parent_Edu"].eq("Below High School")).astype(int) * 10
)

df["Risk_Level"] = df["Risk_Score"].apply(
    lambda x: "Low Risk" if x <= 30 else
              "Medium Risk" if x <= 60 else
              "High Risk"
)

print("\nSubject contributing most to failure:")
print(df[df["Result"]=="Fail"][["Math","Science","English"]].mean())

print("\nLow attendance always failing?")
print(df[df["Attendance"] < 75][["Name","Result"]])

print("\nHigh Risk but Passed:")
print(df[(df["Risk_Level"]=="High Risk") & (df["Result"]=="Pass")])

print("\nAvg Study Hours of High Risk:")
print(df[df["Risk_Level"]=="High Risk"]["Study_Hours"].mean())

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))


df["Improvement_Potential"] = (100 - df["Avg"]) * (df["Attendance"]/100)

print("\nHigh Potential but High Risk:")
print(df[(df["Improvement_Potential"]>50) & (df["Risk_Level"]=="High Risk")])