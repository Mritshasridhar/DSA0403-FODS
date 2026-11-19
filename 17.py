import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load dataset
df = pd.read_csv("18social_media - 18social_media.csv")

# Use title and description columns
text = " ".join(
    df['title'].fillna('').astype(str) + ' ' +
    df['description'].fillna('').astype(str)
)

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords
stop_words = set(stopwords.words('english'))

words = [
    word for word in text.split()
    if word not in stop_words and len(word) > 2
]

# Calculate frequency
freq = Counter(words)

# User input
N = int(input("Enter N: "))

# Top N words
top_words = freq.most_common(N)

print("\nTop Frequent Words")
for word, count in top_words:
    print(f"{word} : {count}")

# Bar chart
words_plot = [item[0] for item in top_words]
counts_plot = [item[1] for item in top_words]

plt.figure(figsize=(10,5))
plt.bar(words_plot, counts_plot, color='skyblue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {N} Frequent Words")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
