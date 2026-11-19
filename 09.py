import pandas as pd

# Load dataset
property_data = pd.read_csv("Exp9 - Exp9.csv")

# 2. Number of properties with more than four bedrooms
count_properties = property_data[property_data['bedrooms'] > 4].shape[0]

print("Properties with more than 4 bedrooms:", count_properties)

# 3. Property with the largest area
largest_property = property_data.loc[property_data['area'].idxmax()]

print("\nProperty with the largest area:")
print(largest_property)
