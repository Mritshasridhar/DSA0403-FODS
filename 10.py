import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Sales.csv")

# Convert Month_sales to datetime
data['Month_sales'] = pd.to_datetime(data['Month_sales'])

# Monthly total sales
monthly_sales = data.groupby('Month_sales')['Total'].sum()

# Line Plot
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index,
         monthly_sales.values,
         marker='o',
         color='red')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(10,5))
plt.bar(monthly_sales.index.astype(str),
        monthly_sales.values,
        color='green')

plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
