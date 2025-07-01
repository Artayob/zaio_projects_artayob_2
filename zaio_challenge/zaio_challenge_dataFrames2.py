import pandas as pd

def create_dataframe_from_dict():
    dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
    }
    return pd.DataFrame(dict)

print(create_dataframe_from_dict())

def create_dataframe_from_lists():
    data = [
    ["Alice", 25, 90],
    ["Bob", 30, 85],
    ["Charlie", 35, 88]
    ]
    dflist = pd.DataFrame(data, columns= ['Name', 'Age', 'Score'])
    return dflist
print(create_dataframe_from_lists())

import numpy as np

def create_dataframe_from_numpy():
    data = np.array([
    ["Alice", 25, 90],
    ["Bob", 30, 85],
    ["Charlie", 35, 88]
    ])
    return pd.DataFrame(data, columns=["Name", "Age", "Score"])

print(create_dataframe_from_numpy())


def create_dataframe_with_dates():
    rng = pd.date_range("2023-01-01", periods=5, freq="D")
    name = ["Alice", "Bob", "Charlie", "David", "Eve"]
    score = [90, 85, 88, 92, 95]
    
    df = pd.DataFrame({'Name': name, 'Score': score}, index=rng)
    df.index.name = 'Date'  # Optional: sets index name as shown in example
    return df

print(create_dataframe_with_dates())