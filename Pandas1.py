import pandas as pd
import numpy as np

# Creating first series 
ser1 = pd.Series([3,4,8,9,5])
print(ser1)
ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e']) # specify index values 
print(ser1)

print("-----------------------------------------------------------------------")

arr= np.array([3,4,8,9,5])
ser1 = pd.Series(arr)
print(ser1)

print("-----------------------------------------------------------------------")

# Creating a series object using a dictionary 
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':4}
ser1 = pd.Series(dict1)
print("Import the whole Dictionary: \n", ser1)
ser1 = pd.Series(dict1, index=['c', 'b']) # Menthion what keys you want
print("Import only specified indexes from the dictionary: \n", ser1)

print("-----------------------------------------------------------------------")

ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print("Print the whole series: \n", ser1)
print("Print the 3rd element: \n", ser1[2])
print("Print the elements between the 2nd and 4th positions: \n", ser1[1:4])

print("-----------------------------------------------------------------------")

ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print("Print a slice using explicite indexes: \n", ser1['b':'d'])

print("-----------------------------------------------------------------------")