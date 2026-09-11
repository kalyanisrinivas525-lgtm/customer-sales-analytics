-- 1. Overall Business Metrics
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales_data;


-- 2. Sales by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 3. Sales by Region
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;


-- 4. Product Performance
SELECT
    Product,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;


-- 5. Customer Performance
SELECT
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;


-- 6. Average Order Value and Profit Margin
SELECT
    SUM(Sales) AS Total_Sales,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales) * 1.0 / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Percent
FROM sales_data;


-- 7. Monthly Sales Analysis
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Month
ORDER BY Month;


-- 8. Profit Margin by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Profit_Margin_Percent
FROM sales_data
GROUP BY Category
ORDER BY Profit_Margin_Percent DESC;
