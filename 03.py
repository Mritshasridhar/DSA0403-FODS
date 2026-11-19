import pandas as pd
import numpy as np

income_df = pd.read_csv("income.csv")

# Convert income "79K" → 79000
income_df['income_num'] = income_df['income'].str.replace("K","").astype(int) * 1000

filtered = income_df[income_df['income_num'] > 80000]

avg_income = np.mean(filtered['income_num'])

print("Average income (proxy for >4 bedrooms):", avg_income)
