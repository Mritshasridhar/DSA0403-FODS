import pandas as pd
import numpy as np

sales_df = pd.read_csv("Sales.csv")

# Extract price column
prices = sales_df['Price'].to_numpy()

avg_price = np.mean(prices)
print("Average price of products sold:", avg_price)
