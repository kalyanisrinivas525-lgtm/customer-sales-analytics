import pandas as pd

file_path = r"C:\Users\Kalyani\OneDrive\Desktop\customer-sales-analytics\data\raw\customer_sales_data.xlsx"

df = pd.read_excel(file_path)

print("===== BASIC INFORMATION =====")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\n===== NUMERICAL SUMMARY =====")

print(df[["Quantity", "Sales", "Profit", "Discount"]].describe())

print("\n===== SALES ANALYSIS =====")

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity:", df["Quantity"].sum())
print("Number of Orders:", df["Order_ID"].nunique())

print("\n===== CATEGORY ANALYSIS =====")

print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\n===== REGION ANALYSIS =====")

print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\n===== PRODUCT ANALYSIS =====")

print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

print("\n===== CUSTOMER ANALYSIS =====")

print(df.groupby("Customer_Name")["Sales"].sum().sort_values(ascending=False))