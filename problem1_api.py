import sqlite3
import requests

# 1. Fetch data from the API
url = "https://fakerapi.it/api/v1/books?_quantity=5"  
response = requests.get(url)

if response.status_code == 200:
    books = response.json()['data']
    
    # 2. Connect to SQLite database 
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # 3. Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year TEXT
        )
    ''')
    
    # 4. Insert data
    for book in books:
        cursor.execute('''
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        ''', (book['title'], book['author'], book['published']))
    
    # 5. Commit and Display
    conn.commit()
    print("Data inserted successfully. Current Database Content:")
    
    cursor.execute('SELECT * FROM books')
    for row in cursor.fetchall():
        print(row)
        
    conn.close()
else:
    print("Failed to retrieve data")
