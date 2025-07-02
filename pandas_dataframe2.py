import pandas as pd
import numpy as np
# Creating a dataframe with dates as indexes 
# Generate a range of dates between 1st Jan 21 to 31st Jan 21

rng = pd.date_range("1/1/2021", periods=31, freq="D")

# Generate two set of 31 random numbers 

s1 = np.random.random(31)
s2 = np.random.random(31)

# Create a dataFrame with the dates as rows

df1 = pd.DataFrame({'Random1': s1, 'Random2': s2})
print(df1.set_index(rng))

print("-------------------------------------------------------------------------------------------")

print(df1.describe())

