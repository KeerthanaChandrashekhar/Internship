import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "marks": ["85", "90", "88"]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["marks"] = df["marks"].astype(int)
print(df.dtypes)  
print(df["marks"].mean())

data = {
    "Joining_Date": ["2024-01-10", "2023-12-05"]
    
}

df = pd.DataFrame(data)
print(df.dtypes)  

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
print(df.dtypes)
print(df["Joining_Date"].dt.year)