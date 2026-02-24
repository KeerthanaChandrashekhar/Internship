import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("1D Numpy Array:", arr)


arr_2d = np.array([[1, 2], [3, 4]])
print("2D Numpy Array:\n", arr_2d)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]])
print("\n ",a)
print("\n ",b)
print("\n ",c)
print("\n ",d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(a.shape)
print(b.shape)
print(c.shape)    
print(d.shape)