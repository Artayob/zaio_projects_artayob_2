import numpy as np

# Creating an arrays that displays the identity
def identity_array(n):
    return np.identity(n)
print(identity_array(4))    

# creating an array with one value
def array_filled_with_value(shape, value):
    return np.full(shape, value)

print(array_filled_with_value((4, 3), 5))

# creating an array filled with zeros
def array_of_zeroes(shape):
    return np.zeros(shape)
print(array_of_zeroes((5, 6)))  

# Creating an array filled with ones
def array_of_ones(shape):
    return np.ones(shape)
print(array_of_ones((5, 6)))