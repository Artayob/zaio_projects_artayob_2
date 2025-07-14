import pandas as pd

def filter_high_scores(df):
    """
    Filters the DataFrame to include names of students with scores > 70.

    Parameters:
        df (pd.DataFrame): A DataFrame with columns "Name" and "Score".

    Returns:
        list: A list of names of students with scores greater than 70.
    """
    # YOUR CODE HERE

    filtered = filter(lambda x: x['Score'] > 70, df.to_dict(orient='records'))
    return [row['Name'] for row in filtered]

df = pd.DataFrame({
    "Name": ['Alice', 'Bob', 'Charlie', 'David'],
    "Score": [65, 85, 70, 90]
})
print(filter_high_scores(df))

from datetime import datetime

def days_between_dates(date1, date2):
    """
    Calculates the absolute difference in days between two dates.

    Parameters:
        date1 (str): The first date in the format "YYYY-MM-DD".
        date2 (str): The second date in the format "YYYY-MM-DD".

    Returns:
        int: The absolute difference in days between the two dates.
    """
    # YOUR CODE HERE
    d1 = datetime.strptime(date1, "%Y-%m-%d").date()
    d2 = datetime.strptime(date2, "%Y-%m-%d").date()
    return abs((d1- d2).days)
print(days_between_dates("2021-01-01", "2021-01-10"))

from datetime import datetime

def convert_to_date(date_str):
    """
    Converts a string in the format "DD-MM-YYYY" to a datetime.date object.

    Parameters:
        date_str (str): The date string in the format "DD-MM-YYYY".

    Returns:
        datetime.date: The corresponding date object.
    """
    # YOUR CODE HERE
    d1 = datetime.strptime(date_str, "%d-%m-%Y").date()
    return d1
print(convert_to_date("15-02-2023"))

import datetime

def format_date(date_obj, format_str):
    """
    Formats a date object according to the given format string.

    Parameters:
        date_obj (datetime.date): The date object to format.
        format_str (str): The format string.

    Returns:
        str: The formatted date as a string.
    """
    return date_obj.strftime(format_str)

# Test
print(format_date(datetime.date(2023, 1, 1), "%d/%m/%Y"))

import pandas as pd

def analyze_date_column(df):
    """
    Analyzes the 'Date' column of the DataFrame, extracting year, month, day, and day of the week.

    Parameters:
        df (pd.DataFrame): A DataFrame with a column 'Date' containing string dates in the format "YYYY-MM-DD".

    Returns:
        pd.DataFrame: The modified DataFrame with additional columns for year, month, day, and day of the week.
    """
    # YOUR CODE HERE
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.day_name()
    return df
data = {
    "Date": ["2023-01-01", "2023-07-14", "2022-12-31"]
}
df = pd.DataFrame(data)

result = analyze_date_column(df)
print(result)