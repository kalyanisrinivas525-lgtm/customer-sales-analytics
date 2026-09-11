import pandas as pd
import sqlite3

# Excel file path
file_path = r"C:\Users\Kalyani\OneDrive\Desktop\customer-sales-analytics\data\raw\customer_sales_data.xlsx"

# Load Excel data
df = pd.read_excel(file_path)

# Create SQLite database
connection = sqlite3.connect("customer_sales.db")

# Load data into SQL table
df.to_sql("sales_data", connection, if_exists="replace", index=False)

print("Database created successfully!")
print("Table 'sales_data' created successfully!")
print("Records loaded:", len(df))

connection.close()
