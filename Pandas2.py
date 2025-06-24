import pandas as pd
import numpy as np

ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print("Print a slice using explicite indexes: \n", ser1['b':'d'])

print("-----------------------------------------------------------------------")

ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print("Print a single element using explicit indexes 'loc':\n",ser1.loc['b'] )
print("Print slice of elements using explicit indexes with 'loc':\n", ser1.loc['b':'d'])

print("-----------------------------------------------------------------------")

# Access elements of a series using iloc
ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print("Print a single element using explicit indexes 'iloc':\n",ser1.iloc[2] )
print("Print slice of elements using explicit indexes with 'iloc':\n", ser1.iloc[1:4])

print("-----------------------------------------------------------------------")

# Access single element of a series object by using the 'iat'
ser1 = pd.Series([3,4,8,9,5], index=['a','b','c','d','e'])
print(ser1.iat[2])

print("-----------------------------------------------------------------------")

# the array atribute returns the arrays equivelant of the series object
# Return python array equivelant of the series 
arr1 = ser1.array
print(arr1)

print("-----------------------------------------------------------------------")

#'Axes' atribute returns the raw axe label i.e. for series object, returns the index labels 
# return thr row axes labels 
axes1 = ser1.axes
print(axes1)

print("-----------------------------------------------------------------------")

# The hasnans attributte returns whether or not there is any nana value in the series.
# Return true if the series has any NaN values, otherwise false 
ser1 = pd.Series([3,4,8,9,5])
print("Check whether ser1 has NaN values: ", ser1.hasnans)
ser1[2]= np.nan
print("Print ser1 \n:", ser1)
print("Check whether ser1 has NaN values: ", ser1.hasnans)

print("-----------------------------------------------------------------------")

# Retuens boolean result if  the values of the elements are incresing
# Print if the series values are monotonic increasing
ser1 = pd.Series([3,4,8,9,5])
print("Check if ser1 is monotonic Increasing ", ser1.is_monotonic_increasing)
ser1 = pd.Series([1,2,3,4,5])
print("Check if ser1 is monotonic increasing after the change ", ser1.is_monotonic_increasing)

print("-----------------------------------------------------------------------")

# Adding 2 series 
ser1 = pd.Series([1,2,2,4,4,6])
ser2 = pd.Series([10,20,20,40,40,60])
print(ser1.add(ser2))

print("-----------------------------------------------------------------------")

# Use append when uou need to concatenate 2 series
# ser1 = pd.Series([1,2,2,4,4,6])
# ser2 = pd.Series([10,20,20,40,40,60])
# print(ser1.combine(ser2))

print("-----------------------------------------------------------------------")


# Filter/Extract Specific elements with date/time index series 
dt_tm = pd.date_range('2020-04-01', periods=5, freq='6H')
ser1 = pd.DataFrame({'A':['Sleep', 'Breakfast', 'Lunch', 'Snacks', 'Dinner']}, index=dt_tm)
print("Series: \n", ser1)
print("\n", ser1.at_time('18:00'))

print("-----------------------------------------------------------------------")

