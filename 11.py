import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Sales.csv")

# Convert Month_sales column to datetime
data['Month_sales'] = pd.to_datetime(data['Month_sales'])

# Calculate total sales for each month
monthly_sales = data.groupby('Month_sales')['Total'].sum().reset_index()

# ------------------ Line Plot ------------------
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales['Month_sales'],
         monthly_sales['Total'],
         marker='o',
         color='blue',
         linewidth=2)

plt.title('Monthly Sales Trend - Line Plot')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


# ------------------ Scatter Plot ------------------
plt.figure(figsize=(10, 5))
plt.scatter(monthly_sales['Month_sales'],
            monthly_sales['Total'],
            color='red',
            s=100)

plt.title('Monthly Sales Trend - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


# ------------------ Bar Plot ------------------
plt.figure(figsize=(10, 5))
plt.bar(monthly_sales['Month_sales'].dt.strftime('%b-%Y'),
        monthly_sales['Total'],
        color='green')

plt.title('Monthly Sales Trend - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)

plt.show()
