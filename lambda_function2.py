numbers = [3, 3, 4, 5, 6, 7, 8, 9, 10]
def filt_gt5(num):
    return num < 5

filt = filter(filt_gt5, numbers)
print(list(filt))
print("-----------------------------------------------------------")

filt = filter(lambda x: x > 5, numbers)
print(list(filt))

print("-----------------------------------------------------------")
from datetime import datetime
from datetime import date

date1 = datetime(2021, 1, 1, 12, 0, 0)
date2 = datetime(2021, 8, 31, 23, 0, 0)

delta = date2 - date1
print("Difference in days: ", delta)
print("Difference in days: ", delta.days)

print("----------------------------------------------------------")

# Convert string date to a date object
datestr = '1 January 2021'
dateobj = datetime.strptime(datestr, "%d %B %Y")
print(dateobj)

print("--------------------------------------------------------------")
# Convert a Datetime string to a date Object

datestr = '1 January 2021, 12:34:22'
dateobj = datetime.strptime(datestr, "%d %B %Y, %H:%M:%S")

# Format the date object and print
print(dateobj.strftime("%m/%d/%Y, %H:%M:%S"))

print("--------------------------------------------------------------")

# current date and time 
now = datetime.now()
print(now)

print("--------------------------------------------------------------")

# Format the current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and Time:", date_time)

print("--------------------------------------------------------------")

# Working with pandas Datetime Object
import pandas as pd
date = pd.to_datetime("1 January, 2021")
print(date)

print("--------------------------------------------------------------")
# Using date range 
date_rng1 = pd.date_range(start='1/1/2021', end='31/01/2021', freq= 'H')
dfd = pd.DataFrame(date_rng1, columns=['date'])
print(dfd)

print("----------------------------------------------------------------")

# Extract components of the Datetime
# Pandas series.dt return an array of Python datetime.date objects
dfd['year'] = dfd['date'].dt.year
dfd['month'] = dfd['date'].dt.month
dfd['day'] = dfd['date'].dt.day
dfd['hour'] = dfd['date'].dt.hour
dfd['minute'] = dfd['date'].dt.minute
dfd['weekday'] = dfd['date'].dt.weekday
dfd['dayofyear'] = dfd['date'].dt.day_of_year

print(dfd)