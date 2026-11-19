import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("20ab_test.csv")

groupA = df[df['Group']=='A']['Conversion']
groupB = df[df['Group']=='B']['Conversion']

t_stat, p_value = ttest_ind(groupA, groupB)

print("T Statistic :", t_stat)
print("P Value :", p_value)

alpha = 0.05

if p_value < alpha:
    print("Statistically Significant Difference Exists")
else:
    print("No Statistically Significant Difference")
