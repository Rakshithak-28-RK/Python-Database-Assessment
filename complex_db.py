import sqlite3
import csv

def create_database():
    conn = sqlite3.connect('complex_books.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER,
            year INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    ''')
    conn.commit()
    return conn

def insert_data(conn, csv_file='books.csv'):
    cursor = conn.cursor()
    # Assume CSV has: title,author,year
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Insert author if not exists
            cursor.execute('INSERT OR IGNORE INTO authors (name) VALUES (?)', (row['author'],))
            author_id = cursor.lastrowid or cursor.execute('SELECT id FROM authors WHERE name = ?', (row['author'],)).fetchone()[0]
            # Insert book
            cursor.execute('INSERT INTO books (title, author_id, year) VALUES (?, ?, ?)', 
                           (row['title'], author_id, int(row['year'])))
    conn.commit()

def query_and_export(conn, output_file='book_report.csv'):
    cursor = conn.cursor()
    # Complex query with join and aggregation
    cursor.execute('''
        SELECT b.title, a.name AS author, b.year, COUNT(*) OVER (PARTITION BY a.id) AS books_by_author
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY a.name, b.year
    ''')
    results = cursor.fetchall()
    
    # Export to CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Author', 'Year', 'Books by Author'])
        writer.writerows(results)
    print(f"Exported {len(results)} records to {output_file}")

# Usage
conn = create_database()
insert_data(conn, 'books.csv')  # Ensure CSV exists with sample data
query_and_export(conn)
conn.close()
