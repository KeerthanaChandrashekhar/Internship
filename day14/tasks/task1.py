import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data.csv')

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])


df_encoded = pd.get_dummies(df, columns=["Color"], drop_first=True)
print(df_encoded)




