import numpy as np

arr1 = np.arange(30).reshape(5,6)
print("printing Through Rows:")
for row in arr1:
    print(row)

print("-------------------------------------------------------------------")

# Iterating through rows 
print("printing through columns:")
cols = arr1.shape[1] # returns the number of columns
for n in range(cols):
    print(arr1[:,n])

print("-------------------------------------------------------------------")

# Horizontal stacking in an array
arr1 = np.arange(30).reshape(5,6)
print("Array 1: \n", arr1)
arr2 = np.arange(100, 130).reshape(5,6)
print("Array 2: \n", arr2)
print("Stcaked Array :\n", np.hstack((arr1, arr2)))

print("-------------------------------------------------------------------")

# Vertical stacking in an array
arr1 = np.arange(30).reshape(5,6)
print("Array 1: \n", arr1)
arr2 = np.arange(100, 130).reshape(5,6)
print("Array 2: \n", arr2)
print("Vertical Stcaked Array :\n", np.vstack((arr1, arr2)))

print("-------------------------------------------------------------------")

# Vertically splitting of 2 arrays
arr1 = np.arange(36).reshape(6,6)
print(arr1, '\n')
splt = np.vsplit(arr1,2)
print(splt[0],'\n')
print(splt[1])

print("-------------------------------------------------------------------")

# Horizontally splitting of 2 arrays
arr1 = np.arange(36).reshape(6,6)
print(arr1, '\n')
splt = np.hsplit(arr1,2)
print(splt[0], '\n')
print(splt[1])


print("-------------------------------------------------------------------")

# Demonstate Array assignment 
arr1 = np.arange(36).reshape(6,6)
arr2 = arr1   # arr2 is a reference to arr1, not a physically different copy 
arr1[1,1]= 99  # Change reflected in both arr1 nd arr2
print("Array 1: \n", arr1)
print("Array 2: \n", arr2)

print("-------------------------------------------------------------------")

# Demonstate Array copy 
arr1 = np.arange(36).reshape(6,6)
arr2 = arr1.copy()  # A physically different copy of the input array is created 
arr1[1,1] = 99      # change reflected in both arr1 and arr2
print("Array 1: \n", arr1)
print("Array 2: \n", arr2)