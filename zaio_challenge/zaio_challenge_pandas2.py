import pandas as pd


def access_using_loc_iloc(series, loc_index, iloc_index):
    loc_value = series.loc[loc_index]
    iloc_value = series.iloc[iloc_index]
    return loc_value, iloc_value

ser1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(access_using_loc_iloc(ser1, 'c', 3))

def access_with_iloc(series, idx):
    return series.iloc[idx]

s = pd.Series([1, 2, 3, 4, 5])
print(access_with_iloc(s, 2))

def access_with_iat(series, idx):
    return series.iat[idx]

    
ser1 = pd.Series([11, 12, 13, 14, 15])
print(access_with_iat(ser1, 2))


def series_attributes(series):
    return{
        'array': series.array,
        'axes': series.axes,
        'dtypes': series.dtype,
        'hasnans': series.hasnans,
        'index': series.index,
        'is_unique': series.is_unique,
        'nbytes': series.nbytes,
        'size': series.size,
        'values': series.values
    }

ser1 = pd.Series([10, 20, 30, 40, 50])
print(series_attributes(ser1))