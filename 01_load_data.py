import pandas as pd

file_path = r"C:\Users\Kalyani\OneDrive\Desktop\customer-sales-analytics\data\raw\customer_sales_data.xlsx"

df = pd.read_excel(file_path)

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Order IDs:")
print(df["Order_ID"].duplicated().sum())

print("\nInvalid Quantity:")
print((df["Quantity"] < 1).sum())

print("\nInvalid Sales:")
print((df["Sales"] <= 0).sum())

print("\nInvalid Profit:")
print((df["Profit"] <= 0).sum())

print("\nInvalid Discount:")
print(((df["Discount"] < 0) | (df["Discount"] > 1)).sum())