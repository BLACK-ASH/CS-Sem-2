import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array  X : ",x)

y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array Y : ",y)

# Array Properties
print("Shape : ",y.shape)
print("Size : ",y.size)
print("Dimension : ",y.ndim)

num = np.arange(1,11,2)
print("Array By Range : ",num)
