import pandas as pd
import numpy as np

stu_df = pd.read_csv("stu (2) - stu (2).csv")

prices = stu_df['Math'].fillna(0).to_numpy()
quantities = stu_df['Science'].fillna(0).to_numpy()

discount_rate = 10
tax_rate = 5

subtotal = np.sum(prices * quantities)
discount_amount = subtotal * (discount_rate / 100)
tax_amount = (subtotal - discount_amount) * (tax_rate / 100)

total_cost = subtotal - discount_amount + tax_amount

print("Total cost:", total_cost)
