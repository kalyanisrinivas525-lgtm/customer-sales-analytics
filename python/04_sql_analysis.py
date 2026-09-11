import sqlite3

connection = sqlite3.connect("customer_sales.db")
cursor = connection.cursor()

# 1. Overall metrics
query = """
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales_data;
"""

cursor.execute(query)
result = cursor.fetchone()

print("===== OVERALL BUSINESS METRICS =====")
print("Total Sales:", result[0])
print("Total Profit:", result[1])
print("Total Quantity:", result[2])
print("Total Orders:", result[3])


# 2. Sales by Category
query = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)

print("\n===== SALES BY CATEGORY =====")

for row in cursor.fetchall():
    print(row)


# 3. Sales by Region
query = """
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)

print("\n===== SALES BY REGION =====")

for row in cursor.fetchall():
    print(row)


# 4. Top Products
query = """
SELECT
    Product,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)

print("\n===== PRODUCT PERFORMANCE =====")

for row in cursor.fetchall():
    print(row)


# 5. Customer Performance
query = """
SELECT
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)

print("\n===== CUSTOMER PERFORMANCE =====")

for row in cursor.fetchall():
    print(row)
    # 6. Average Order Value and Profit Margin
query = """
SELECT
    SUM(Sales) AS Total_Sales,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales) * 1.0 / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Percent
FROM sales_data;
"""

cursor.execute(query)

result = cursor.fetchone()

print("\n===== BUSINESS KPIs =====")
print("Total Sales:", result[0])
print("Total Orders:", result[1])
print("Average Order Value:", result[2])
print("Total Profit:", result[3])
print("Profit Margin:", result[4], "%")
# 7. Monthly Sales Analysis
query = """
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Month
ORDER BY Month;
"""

cursor.execute(query)

print("\n===== MONTHLY SALES ANALYSIS =====")

for row in cursor.fetchall():
    print(row)


# 8. Profit Margin by Category
query = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Percent
FROM sales_data
GROUP BY Category
ORDER BY Profit_Margin_Percent DESC;
"""

cursor.execute(query)

print("\n===== PROFIT MARGIN BY CATEGORY =====")

for row in cursor.fetchall():
    print(row)


connection.close()
