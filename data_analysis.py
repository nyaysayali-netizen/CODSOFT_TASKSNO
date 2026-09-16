import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== BUSINESS QUESTIONS ==========")

total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
average_sales = df["Sales"].mean()
print("Average Sales per Order:", round(average_sales, 2))

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(product_sales)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)
print("\n========== OUTLIER DETECTION ==========")
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("\nOutliers:")
print(outliers)
print("\n========== CORRELATION ==========")
correlation = df[["Quantity", "Unit_Price", "Sales"]].corr()
print(correlation)
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
df["Sales"].plot(kind="hist", bins=8)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()