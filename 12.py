import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("12.Temprain.csv")

# Monthly averages
monthly_temp = data.groupby('Month')['tem'].mean().reset_index()
monthly_rain = data.groupby('Month')['rain'].mean().reset_index()

# Line Plot - Temperature
plt.figure(figsize=(10, 5))
plt.plot(monthly_temp['Month'],
         monthly_temp['tem'],
         marker='o',
         color='blue')

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter Plot - Rainfall
plt.figure(figsize=(10, 5))
plt.scatter(monthly_rain['Month'],
            monthly_rain['rain'],
            color='red',
            s=100)

plt.title("Monthly Average Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
