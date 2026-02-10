import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,3])

arr_3d = np.array([[[1 , 2, 3], [4, 5, 6]], 
                   [[7, 8, 9], [10, 11, 12]]])
print(arr_3d[0, 1, 2])


arr_1d = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr_1d[1:5])