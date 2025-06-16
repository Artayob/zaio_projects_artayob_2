import numpy as np

arr = np.array([[1,2,3,4,5], [2,3,4,5,6]])
print(arr)
print(arr.shape)

print("------------------------------------------------------------------")

# Create an array of all zeros
arr = np.zeros((4,4)) # you can do the same for ones eg arr = np.ones((3,4))
print(arr)

print("------------------------------------------------------------------")

# Create an array filling all elements with a specified vales 
arr = np.full((4,3), 9)
print(arr)

print("------------------------------------------------------------------")

# Create a 4x4 identity matrix
arr = np.eye(4)
print(arr)

print("------------------------------------------------------------------")

# Create an array filled with random values 
arr = np.random.random((3,3))
print(arr)

print("------------------------------------------------------------------")

# Create an array with sequential values starting from a given range 
arr = np.arange(30)
print(arr)

print("------------------------------------------------------------------")

arr = np.arange(0,30, 2)
print(arr)

print("------------------------------------------------------------------")

# reshape the array to a new specified dimension 
arr = np.arange(30)
arr = arr.reshape(5,6)
print(arr)

print("------------------------------------------------------------------")

# Creating a string array
arr = np.array([['John', 'Robert'], ['Pranav', 'Tauseef']])
print(arr)

print("------------------------------------------------------------------")

# Return the dot product of 2 arrays 
arr1 =np.arange(30).reshape(5,6)
arr2 = arr1.T
arr_res = arr1.dot(arr2)
print(arr_res)

print("------------------------------------------------------------------")

# Flatten an array 
arr1 =np.arange(30).reshape(5,6)
arr = arr1.flatten()
print(arr)

print("------------------------------------------------------------------")