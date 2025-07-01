#### STUDENT CODE CELL
import pandas as pd

def load_and_inspect_data():
    data = {
        "OrderID": [1001, 1002, 1003, 1004, 1005],
        "Product": ["Laptop", "Smartphone", "Office Chair", "Desk", "Microwave"],
        "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Appliances"],
        "Customer": ["Alice Smith", "Bob Johnson", "Charlie Lee", "David Brown", "Eve Wilson"],
        "Quantity": [2, 1, 5, 1, 1],
        "Price": [800, 600, 120, 200, 150],
        "Discount": [10, 5, 15, 0, 10],
        "Total": [1440, 570, 510, 200, 135],
        "Region": ["North", "South", "East", "West", "North"],
        "Date": ["2023-01-15", "2023-01-18", "2023-01-20", "2023-02-01", "2023-02-15"]
    }
    df = pd.DataFrame(data)


    dtype_map = {
        "int64": int,
        "float64": float,
        "object": object
    }
    column_info = {
        "Column Names": df.columns.tolist(),
        "Data Types": {col: dtype_map.get(str(df[col].dtype), object) for col in df.columns}
    }
    first_rows = df.head()
    return column_info, first_rows

print(load_and_inspect_data())




def handle_missing_values():
    data = {
        "OrderID": [1001, 1002, 1003, 1004, 1005],
        "Product": ["Laptop", None, "Office Chair", "Desk", "Microwave"],
        "Category": ["Electronics", "Electronics", "Furniture", "Furniture", None],
        "Customer": ["Alice Smith", "Bob Johnson", "Charlie Lee", None, "Eve Wilson"],
        "Quantity": [2, 1, 5, None, 1],
        "Price": [800, 600, 120, 200, None],
        "Discount": [10, 5, None, 0, 10],
        "Total": [1440, None, 510, 200, 135],
        "Region": ["North", "South", "East", None, "North"],
        "Date": ["2023-01-15", "2023-01-18", "2023-01-20", "2023-02-01", "2023-02-15"]
    }

    df = pd.DataFrame(data)


    missing_counts = df.isnull().sum()

    # Fill missing values correctly
    df["Product"] = df["Product"].fillna("Unknown")
    df["Category"] = df["Category"].fillna("Unknown")
    df["Customer"] = df["Customer"].fillna("Not Specified")
    df["Region"] = df["Region"].fillna("Not Specified")
    df["Quantity"] = df["Quantity"].fillna(0)
    df["Price"] = df["Price"].fillna(0)
    df["Discount"] = df["Discount"].fillna(df["Discount"].mean())
    df["Total"] = df["Total"].fillna(df["Total"].mean())

    return missing_counts, df


    return df, missing_counts
print(handle_missing_values())



def aggregate_and_group():
    data = {
        "Region": ["North", "South", "East", "West", "North", "South"],
        "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Appliances", "Appliances"],
        "Sales": [1200, 800, 950, 650, 400, 300],
        "Profit": [200, 150, 120, 50, 60, 40]
    }

    df = pd.DataFrame(data)
    grouped_data = df.groupby(["Region", "Category"]).agg({
        "Sales": "sum",
        "Profit": "mean"
    }).reset_index()
    grouped_data = grouped_data.rename(columns={
        "Sales": "TotalSales",
        "Profit": "AvgProfit"
    })
    return grouped_data
print(aggregate_and_group())



def create_sales_pivot_table():
    # Define the dataset
    data = {
        "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
        "Category": ["Electronics", "Electronics", "Furniture", "Furniture",
                     "Appliances", "Appliances", "Electronics", "Furniture"],
        "Sales": [1200, 800, 950, 650, 400, 300, 1500, 700],
        "Profit": [200, 150, 120, 50, 60, 40, 300, 100]
    }
    df = pd.DataFrame(data)
    pivot = pd.pivot_table(
        df,
        values="Sales",
        index="Region",
        columns="Category",
        aggfunc="sum",
        fill_value=0
    )

    return pivot
print(create_sales_pivot_table())