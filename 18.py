import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load dataset
df = pd.read_csv("21bodyfat - 21bodyfat.csv")

# Select required columns
data = df[['Age', 'BodyFat']]

print("First 5 Records")
print(data.head())

# Mean
print("\nMean")
print(data.mean())

# Median
print("\nMedian")
print(data.median())

# Standard Deviation
print("\nStandard Deviation")
print(data.std())

# Boxplots
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.boxplot(data['Age'])
plt.title("Boxplot of Age")

plt.subplot(1,2,2)
plt.boxplot(data['BodyFat'])
plt.title("Boxplot of Body Fat")

plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(6,5))
plt.scatter(data['Age'], data['BodyFat'],
            color='blue')
plt.xlabel("Age")
plt.ylabel("Body Fat")
plt.title("Age vs Body Fat")
plt.grid(True)
plt.show()

# Q-Q Plot for Age
stats.probplot(data['Age'],
               dist="norm",
               plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

# Q-Q Plot for Body Fat
stats.probplot(data['BodyFat'],
               dist="norm",
               plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()
