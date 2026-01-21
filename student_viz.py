import matplotlib.pyplot as plt

def visualize_student_scores():
    # Mock dataset (Replace this list with an API call if a URL is provided)
    students = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 76},
        {"name": "Charlie", "score": 92},
        {"name": "Diana", "score": 85},
        {"name": "Evan", "score": 67}
    ]

    # Extract data for plotting
    names = [s['name'] for s in students]
    scores = [s['score'] for s in students]

    # Calculate average
    avg_score = sum(scores) / len(scores)
    print(f"Average Score: {avg_score:.2f}")

    # Create Bar Chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, scores, color='skyblue', edgecolor='black')
    
    # Add a horizontal line for the average
    plt.axhline(y=avg_score, color='r', linestyle='--', label=f'Average ({avg_score:.2f})')

    plt.xlabel('Students')
    plt.ylabel('Scores')
    plt.title('Student Test Scores')
    plt.legend()
    plt.ylim(0, 100)
    
    # Show value on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

    plt.show()

if __name__ == "__main__":
    visualize_student_scores()
