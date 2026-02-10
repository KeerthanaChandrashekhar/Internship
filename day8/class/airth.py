import numpy as np

a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#broadcasting with scalar
arr = np.array([10, 20, 30])
print("Addition with scalar:", arr + 5)

# scalar is broadcast logically no extra memory is created

#broadcasting with different shapes

