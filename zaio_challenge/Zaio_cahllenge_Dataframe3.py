import pandas as pd

def apply_describe_method():
    data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [90, 85, 88, 92, 95]
    } 
    df = pd.DataFrame(data)
    return df.describe()
print(apply_describe_method())

def apply_transpose_method():
    data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
    }
    df = pd.DataFrame(data)
    return df.transpose()
print(apply_transpose_method())

def apply_sort_values_method():
    data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [90, 85, 88, 92, 95]
    }
    df = pd.DataFrame(data)
    return df.sort_values("Score", ascending=False)

print(apply_sort_values_method())

def select_data_from_dataframe():
    data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [90, 85, 88, 92, 95]
    }
    df = pd.DataFrame(data)
    return df[["Name","Score"]]
print(select_data_from_dataframe())

def select_data_with_condition():
    data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [90, 85, 88, 92, 95]
    }
    df = pd.DataFrame(data)
    return df[df["Score"] > 88]
print(select_data_with_condition())   

def select_data_with_multiple_conditions():
    data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "Score": [90, 85, 88, 92, 95]
    }
    df = pd.DataFrame(data)
    return df[(df["Score"] > 88) & (df["Age"] <= 40)]
print(select_data_with_multiple_conditions())