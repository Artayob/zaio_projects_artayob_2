import numpy as np

# Return the dot product of 2 arrays 
arr1 =np.arange(30).reshape(5,6)
print(arr1)
arr2 = arr1.T
print(arr2)
arr_res = arr1.dot(arr2)
print(arr_res)

print("------------------------------------------------------------------")

arr1 =np.arange(30).reshape(5,6)
arr = arr1.flatten()
print(arr)

print("------------------------------------------------------------------")

arr1 =np.arange(30).reshape(5,6)
minm = arr1.min()
maxm = arr1.max()
mean = arr1.mean()
std = arr1.std(axis=1)
var = arr1.var(axis=0)
print("Minimum:", minm)
print("Maximum:", maxm)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Variance:", var)

print("------------------------------------------------------------------")

arr1 =np.arange(30).reshape(5,6)
arrc = arr1.copy()
print(arrc)

print("------------------------------------------------------------------")

# Rounding elements 
arr1 = np.random.random((3,3))
print("Array 1: \n", arr1)
arr2 = arr1.round(2)
print("Array 2: \n", arr2)

print("------------------------------------------------------------------")

arr1 =np.arange(30).reshape(5,6)
print("Array 1: \n", arr1)
arr2 = arr1.astype(str)
print("Array 2: \n", arr2)
arr3 = arr2.astype(int)
print("Array 3: \n", arr3)

print("------------------------------------------------------------------")

# Accessing array elements 
arr1 =np.arange(30).reshape(5,6)
print("Array 1: \n", arr1)
print("Element at the 2nd row, 3rd column: ", arr1[1, 2])

print("------------------------------------------------------------------")

# Accessing array elements 
arr1 =np.arange(30).reshape(5,6)
print("Array 1: \n", arr1)
print("Elements on the 2nd row, 3rd to 5th positions: ", arr1[1, 2:5])

print("---------------------------------------------------------------------")

arr1 = np.arange(64).reshape(4,4,4)
print("Array 1:",  arr1)
print("Elements at the first positions: first dimension: 0, second dimension: 3, third Dimension: 2")
print(arr1[0, 3, 2])
print("Elements at the first positions: first dimension: 0, second dimension: positions first to second, third Dimension: 2")
print(arr1[0, 0:2, 2])