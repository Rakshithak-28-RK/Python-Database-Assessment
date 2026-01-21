import matplotlib.pyplot as plt
import pandas as pd

# Mock data (Simulating API response)
data = {
    "students": [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "Diana", "score": 88},
        {"name": "Evan", "score": 95}
    ]
}

# 1. Process Data
df = pd.DataFrame(data['students'])
average_score = df['score'].mean()
print(f"Average Class Score: {average_score}")

# 2. Visualize Data
plt.figure(figsize=(8, 5))
colors = ['skyblue' if x >= average_score else 'salmon' for x in df['score']]

plt.bar(df['name'], df['score'], color=colors)
plt.axhline(average_score, color='red', linestyle='--', label=f'Average ({average_score})')

plt.xlabel('Student Name')
plt.ylabel('Score')
plt.title('Student Test Scores')
plt.legend()
plt.show()
