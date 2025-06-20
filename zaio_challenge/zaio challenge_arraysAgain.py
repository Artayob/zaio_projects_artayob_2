import numpy as np

def array_statistics(arr):
    arr = np.array(arr)
    stats = {
        'min': float(np.min(arr)),  
        'max': float(np.max(arr)),  
        'mean': float(np.mean(arr)),
        'std': float(np.std(arr)),
        'var': float(np.var(arr))
    }
    return stats

print(array_statistics(np.array([1, 2, 3, 4])))

def copy_array(arr):
    return np.copy(arr)

arr = np.array([1,4,7])
copy_arr = copy_array(arr)
print(copy_arr)

def round_elements(arr, decimals):
    arr1 = np.array(arr)
    return np.round(arr1, decimals)

print(round_elements(np.array([1.225,4.555,7.410]),2))

def convert_dtype(arr, dtype):
    return np.array(arr).astype(dtype)


print(convert_dtype(np.array([1, 2, 3]), float)) 
print(convert_dtype(np.array([1.1, 2.2, 3.3]), int))  
print(convert_dtype(np.array([1, 0]), bool)) 