import pandas as pd
import re
from collections import Counter

# Read dataset
df = pd.read_csv("13.ADANIPORTS.csv")

# Convert all values to strings and join them
text = " ".join(map(str, df.values.flatten()))

# Convert to lowercase
text = text.lower()

# Remove special characters and numbers
text = re.sub(r'[^a-zA-Z\s]', ' ', text)

# Split into words
words = text.split()

# Calculate word frequency
freq_dist = Counter(words)

# Display the 20 most common words
print("Word Frequency Distribution:\n")

for word, count in freq_dist.most_common(20):
    print(f"{word}: {count}")
