import numpy as np
import pandas as pd

df = pd.read_csv("student_scores.csv")

# Convert to NumPy array (Math, Science, English, History)
student_scores = df[['Math','Science','English','History']].to_numpy()

# Average score per subject
avg_scores = np.mean(student_scores, axis=0)

subjects = ['Math','Science','English','History']
highest_subject = subjects[np.argmax(avg_scores)]

print("Average scores:", avg_scores)
print("Highest average subject:", highest_subject)
