import pandas as pd

def join_two_dataframes():
    df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
    })
    df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Score": [85, 88, 92]
    })
    left_join = pd.merge(df1, df2, how='left', on='ID')
    right_join = pd.merge(df1, df2, how='right', on='ID')
    return left_join, right_join

print(join_two_dataframes())

def join_dataframes_with_nonmatching_keys():
  
    df1 = pd.DataFrame({
        "EmployeeID": [101, 102, 103],
        "Name": ["Alice", "Bob", "Charlie"],
        "Department": ["HR", "IT", "Finance"]
    })
    df2 = pd.DataFrame({
        "EmpID": [102, 104, 105],
        "Salary": [70000, 80000, 75000]
    })
    left_join_result = pd.merge(df1, df2, how="left", left_on="EmployeeID", right_on="EmpID")
    right_join_result = pd.merge(df1, df2, how="right", left_on="EmployeeID", right_on="EmpID")
    return left_join_result, right_join_result
    
print(join_dataframes_with_nonmatching_keys())