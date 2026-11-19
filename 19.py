import pandas as pd
import scipy.stats as stats
import numpy as np

# Dataset should contain:
# Group,Reduction

df = pd.read_csv("19bloodpressure.csv")

drug = df[df['Group'] == 'Drug']['Reduction']
placebo = df[df['Group'] == 'Placebo']['Reduction']

# Drug CI
mean_d = np.mean(drug)
sem_d = stats.sem(drug)

ci_d = stats.t.interval(
    0.95,
    len(drug)-1,
    loc=mean_d,
    scale=sem_d
)

# Placebo CI
mean_p = np.mean(placebo)
sem_p = stats.sem(placebo)

ci_p = stats.t.interval(
    0.95,
    len(placebo)-1,
    loc=mean_p,
    scale=sem_p
)

print("Drug Group 95% CI:")
print(ci_d)

print("\nPlacebo Group 95% CI:")
print(ci_p)
