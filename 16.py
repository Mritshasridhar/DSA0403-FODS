import pandas as pd
from collections import Counter
import re

# Load dataset
df = pd.read_csv("16bbc-text - 16bbc-text.csv")

# Combine all text rows
text = " ".join(df.astype(str).fillna('').values.flatten())

# Preprocessing
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

# Word frequency
words = text.split()
freq = Counter(words)

# Display top 20 words
print("Top 20 Frequent Words:")
for word, count in freq.most_common(20):
    print(word, ":", count)
