import numpy as np

arr = np.arange(40, 55, 3)
print("Array of numbers:" , arr)

print(arr.shape)

arr_1 = np.arange(1, 17).reshape(4, 4)
print(arr_1)

arr_2 = np.linspace(0, 7, 5)
print(arr_2)

arr_3 = np.random.rand(2, 2)
print(arr_3)

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)
