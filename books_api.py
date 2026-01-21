import requests
import sqlite3

def fetch_and_store_books():
    # Using a public placeholder API for demonstration
    api_url = "https://fakerapi.it/api/v1/books?_quantity=5"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()['data'] # Adjust key based on actual API structure

        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect('books_data.db')
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                published_date TEXT
            )
        ''')

        # Insert data
        for book in data:
            cursor.execute('''
                INSERT INTO books (title, author, published_date)
                VALUES (?, ?, ?)
            ''', (book['title'], book['author'], book['published']))

        conn.commit()
        print("Data stored successfully.\n")

        # Display retrieved data
        print("--- Stored Books ---")
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | Date: {row[3]}")

        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_store_books()
