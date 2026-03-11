import pandas as pd
import os
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

path = kagglehub.dataset_download("yasserh/wine-quality-dataset")
print("Dataset path:", path)

df = pd.read_csv(os.path.join(path, "WineQT.csv"))

print(df.head())
print(df.info())

X = df.drop(["quality", "Id"], axis=1)
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)