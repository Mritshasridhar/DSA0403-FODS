import pandas as pd
data = pd.read_csv("Exp8.csv")
df = pd.DataFrame(data)

top_5_products = df.groupby('product_name')['quantity'].sum().nlargest(5)

print("Top 5 Products by Quantity Sold:")
print(top_5_products)
