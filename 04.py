import pandas as pd
import numpy as np

fuel_df = pd.read_csv("Fuel_Efficiency datasets.csv")

# Take combination_mpg as quarterly performance
quarter_data = fuel_df['combination_mpg'].head(4).to_numpy()

total_year = np.sum(quarter_data)
percent_increase = ((quarter_data[3] - quarter_data[0]) / quarter_data[0]) * 100

print("Total yearly performance:", total_year)
print("Percentage increase Q1 to Q4:", percent_increase)
