import pandas as pd

# Read dataset
df = pd.read_csv("14.score_updated.csv")

# Frequency distribution of ages
age_frequency = df['age'].value_counts().sort_index()

print("Frequency Distribution of Ages:\n")
print(age_frequency)
