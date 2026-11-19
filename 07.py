import pandas as pd

sales_df = pd.read_csv("Sales.csv")

# 1. Total number of orders per Sales Rep
orders_per_rep = sales_df.groupby('Sales_Rep').size()

# 2. Average quantity sold per product
avg_qty_product = sales_df.groupby('Product_Name')['Quantity_Sold'].mean()

# 3. Earliest & latest month in dataset
earliest = sales_df['Month_sales'].min()
latest = sales_df['Month_sales'].max()

print("Orders per Sales Rep:\n", orders_per_rep)
print("\nAverage quantity per product:\n", avg_qty_product)
print("\nEarliest month:", earliest)
print("Latest month:", latest)
