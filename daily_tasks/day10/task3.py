import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", " los angeles", "LOS ANGELES "]
}

df = pd.DataFrame(data)

df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.lower() 

print(df["Location"])
print(df["Location"].unique())