#### STUDENT CODE CELL

import numpy as np
# Creating a 2d array
def tuple_to_2d_array(tup):
    return np.array(tup)
    ##raise NotImplementedError()
print(tuple_to_2d_array(((1, 2), (3, 4))).tolist())
print(tuple_to_2d_array(((5, 6), (7, 8))).tolist())  

# Creating a 1d array
def tuple_to_1d_array(tup):
    return np.array(tup)
    ###raise NotImplemented,Error(),

print(tuple_to_1d_array((1, 2, 3)))

print(tuple_to_1d_array((4, 5, 6, 7)))

# converting an empty tuple t an empty array
def tuple_to_empty_array(tup):
    shape = np.shape(tup)
    return np.empty(shape)