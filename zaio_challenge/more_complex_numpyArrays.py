import numpy as np

# Itterating an array
def iterate_array(arr):
    for row in arr:
        print(f"Row: {[int(i) for i in row]}")
    for col in arr.T:
        print(f"Column: {[int(i) for i in col]}")

arr = np.array([[1, 5], [3, 4]])
iterate_array(arr)

print("----------------------------------------------------------------------------")
# Stacking an array
def horizontal_stack(arr1, arr2):
    return np.hstack((arr1,arr2))

def vertical_stack(arr1, arr2):
    return np.vstack((arr1,arr2))

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(horizontal_stack(arr1, arr2))
print(vertical_stack(arr1,arr2))

print("------------------------------------------------------------------------------")

# Splitting an array
def horizontal_split(arr, num_splits):
    return np.hsplit(arr, 2)

def vertical_split(arr, num_splits):
    return np.vsplit(arr, 3)

arr = np.arange(30).reshape(3,10)
num_splits = 3
print(horizontal_split(arr, num_splits))
print(vertical_split(arr, num_splits))