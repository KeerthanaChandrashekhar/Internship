import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('pizza_data.csv')

x = data[['diameter', 'toppings']]
y = data['price']

model = LinearRegression()
model = model.fit(x, y)

prediction = model.predict([[10, 2]])
print("Predicted Pizza Price:", prediction[0])

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)