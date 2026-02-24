import pandas as pd

products = pd.Series([ 700, 150, 300], index = ['Laptop', 'Mouse', 'Keyboard'])
print(products)

print("\n", products['Laptop'])

print("\n", products[0:2])