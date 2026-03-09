from sklearn.tree import DecisionTreeRegressor

# Features
X = [
    [1.34,0.34],
    [3.45,1.45],
    [1.69,0.98],
    [2.56,1.79],
    [3.00,1.13],
    [1.30,0.88]
]

# Target (numeric value)
y = [15,42,20,35,40,16]

model = DecisionTreeRegressor()
model.fit(X,y)

prediction = model.predict([[2.8,1.2]])
print("Predicted height:", prediction)