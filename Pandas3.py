import pandas as pd
import numpy as np

# between returns a boolean for the values eg
ser1 = pd.Series([1, 2, 3, 4, 5, 6])
print(ser1.between(2,4))

print("---------------------------------------------------------------------------")

# Copies one series to another 

ser1 = pd.Series([1, 2, 3, 4, 5, 6])
ser2 = ser1.copy(deep=True)
ser1[2] =8
print("Ser1: \n", ser1)
print("Ser2 - Deep copy: \n", ser2)
ser3 = ser1.copy(deep=False)
ser1[2]= 8
print("ser3 - shallow copy: \n", ser3)

print("---------------------------------------------------------------------------")

# Prints descriptive statistics of the series 
ser1 = pd.Series([1, 2, 3, 4, 5, 6])
print(ser1.describe())

print("---------------------------------------------------------------------------")

# Divide corresponding elements from 2 series 

ser1 = pd.Series([5, 4, 52, 64, 47, 45])
ser2 = pd.Series([10, 20, 20, 40, 40, 60])
print(round(ser1.div(ser2),2))

print("---------------------------------------------------------------------------")

# The drop method removes elements 
ser1 = pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])
ser2 = ser1.drop(labels=['c', 'e'])
print(ser2)

print("---------------------------------------------------------------------------")
# Equals checks if its equal

ser1 = pd.Series([1, 2, 3, 4, 5, 6])
ser2 = pd.Series([1, 2, 3, 4, 5, 6])
print(ser1.equals(ser2))

print("---------------------------------------------------------------------------")

# fillna fills the NaN values 
ser1 = pd.Series([1,2,3,4,5,6])
ser1[2] = np.nan
print("Print ser1 \n", ser1)
print("Check the series after filling NaNs: \n", ser1.fillna(12))

print("---------------------------------------------------------------------------")

# Floordiv
ser1 = pd.Series([5, 4, 52, 64, 47, 45])
ser2 = pd.Series([10, 20, 20, 40, 40, 60])
print(round(ser1.floordiv(ser2)))

print("---------------------------------------------------------------------------")

# Groupby 
ser1 = pd.Series([23, 34, 56, 76, 53, 54], index=['HR', 'SALES', 'HR', 'SALES', 'HR', 'SALES'])
print(ser1.groupby(level=0).mean())

print("---------------------------------------------------------------------------")

# The idxmax method returns the label or index of the maximum value 
ser1 = pd.Series([23, 34, 56, 76, 53, 54, 55, 87], index=['HR','FIN', 'SALES','MKTG', 'MANU', 'ADVT', 'OPS', 'QLTY'])
print(ser1.idxmax())

print("---------------------------------------------------------------------------")

# The idxmin method returns the label or index of the minimum value 
ser1 = pd.Series([23, 34, 56, 76, 53, 54, 55, 87], index=['HR','FIN', 'SALES','MKTG', 'MANU', 'ADVT', 'OPS', 'QLTY'])
print(ser1.idxmin())

print("---------------------------------------------------------------------------")

# Checks for nones
ser1 = pd.Series([23, 34, 56, None, 53, 54, 55, 87])
print(ser1.isna())

print("---------------------------------------------------------------------------")

# Checks for a number
ser1 = pd.Series([23, 34, 56, None, 53, 54, 55, 87])
print(ser1.isin([87]))

print("---------------------------------------------------------------------------")

# Return 'max', 'min', 'mean', 'median' values of a Series

ser1 = pd. Series([23, 34, 56, 43, 53, 54, 55, 87])
print("The Maximum aximum Value Valu element: ", ser1.max())
print("The Minimum Value element: ", ser1.min())
print("The Mean of all elements: ", ser1.mean())
print("The Median value among all elements: ", ser1.median())

print("---------------------------------------------------------------------------")

ser1 = pd.Series([1, 2, 3, 4, 5, 6])
ser2 = pd.Series([10, 20, 30, 40, 50, 60])
print(ser1.multiply(ser2))

print("---------------------------------------------------------------------------")

# The 'replace' method replaces a specified value in the Series with another. The 'replace' method returns a 
# modified Series and the original series remains unchanged. The 'inplace' parameter has to be set to True ## if the original Series object is to be updated.
# Replace a spcified value in the Series with another
ser1 = pd.Series([23, 34, 56, 56, 66, 53, 54, 55, 87])
ser2 = ser1. replace({34:55})
print("Printing ser2: \n", ser2)
ser1.replace({34:55}, inplace=True)
print("Printing ser1 after replacing inplace:\n", ser1)

print("---------------------------------------------------------------------------")