import pandas as pd
import numpy as np

list1 = [
    ['Ford', 20000, 'Ecosport'],
    ['Toyota', 22000, 'Fortuner'],
    ['Renault', 31000, 'Duster'],
    ['Tata', 27000, 'Nexion'],
    ['Mahinndra', 19000, 'Scorpio']
]
dflist = pd.DataFrame(list1, columns=['Car_brand', 'Avg_yearly_sale', 'Best_selling_model'])
print(dflist)

print("-------------------------------------------------------------------------------------------")

series1 = pd.Series(['Ford', 'Toyota', 'Renault', 'Tata', 'Mahinndra'])
series2 = pd.Series([20000, 22000, 31000, 27000, 19000])
series3 = pd.Series(['Ecosport', 'Fortuner', 'Duster', 'Nexion', 'Scorpio'])
dictionary_of_nparray = {"Name": series1, "Age": series2, "Department": series3}
dfser = pd.DataFrame(dictionary_of_nparray)
print(dfser)

print("-------------------------------------------------------------------------------------------")

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

