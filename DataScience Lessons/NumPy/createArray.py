import numpy as np

array=np.array([1,2,3], float)

print(array)
print("")
array = np.array([[1, 2, 3], [4, 5, 6]], float) 
# a 2D array/Matrix
print(array)
print("")
array2 = np.array([1, 4, 5, 8], float)

print(array2[1])
print("")
print(array2[:2])
array2[1] = 5.0
print("")
print(array2[1])