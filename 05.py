import pandas as pd
import numpy as np

fuel_df = pd.read_csv("Fuel_Efficiency datasets.csv")

mpg = fuel_df['highway_mpg(Fuel Efficiency)'].to_numpy()

avg_mpg = np.mean(mpg)

model1 = mpg[0]
model2 = mpg[10]

percent_improvement = ((model2 - model1) / model1) * 100

print("Average fuel efficiency:", avg_mpg)
print("Percentage improvement:", percent_improvement)
