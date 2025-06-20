import numpy as np

def random_array(shape):
    return np.random.random(shape)

print(random_array((2,3)))    

def sequential_array(n):
    return np.arange(n)
print(sequential_array(5))    

def sequential_array_with_step(start, end, step):
    return np.arange(start, end, step)
print(sequential_array_with_step(2,10,2))