import pandas as pd

# Load dataset
df = pd.read_csv("TikTok-datasets.csv")

# Frequency distribution of likes
likes_freq = df['num_likes'].value_counts().sort_index()

print("Frequency Distribution of Likes:\n")
print(likes_freq)
