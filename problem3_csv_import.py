import csv
import sqlite3

# 1. Setup Database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')

# 2. Read CSV and Insert (Assuming 'users.csv' exists)
# Create a dummy CSV for this example
with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email'])
    writer.writerow(['John Doe', 'john@example.com'])
    writer.writerow(['Jane Smith', 'jane@test.com'])

# Actual processing code
with open('users.csv', 'r') as file:
    # Skip header if present
    csv_reader = csv.reader(file)
    next(csv_reader) 
    
    for row in csv_reader:
        if row: # Check for empty rows
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (row[0], row[1]))

conn.commit()
print("CSV data imported successfully.")
conn.close()
