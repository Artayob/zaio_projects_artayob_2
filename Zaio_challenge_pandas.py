import pandas as pd

def add_series(s1, s2):
    return s1.add(s2)

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
print(add_series(s1, s2))


def convert_series_dtype(series, dtype):
    return series.astype(dtype)
ser1 = pd.Series([1,2,3,4,5])
print(convert_series_dtype(ser1, 'float'))

def create_date_range(start, end, freq):
    return pd.Series(pd.date_range(start= start, end= end, freq=freq))
create_date_range('2025-06-24', '2025-06-30', 'D')
print(create_date_range('2025-06-24', '2025-06-30', 'D'))