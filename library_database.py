# Day 11: Library Management System
# SQLite Database Connection

import sqlite3

# Connect to the database
connection = sqlite3.connect("library.db")

# Create a cursor
cursor = connection.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    available INTEGER DEFAULT 1
)
""")

# Insert sample books
sample_books = [
    (101, "Python Basics", "John", 1),
    (102, "Machine Learning", "David", 1),
    (103, "Artificial Intelligence", "Smith", 1)
]

cursor.executemany("""
INSERT OR IGNORE INTO books
(book_id, title, author, available)
VALUES (?, ?, ?, ?)
""", sample_books)

# Save changes
connection.commit()

# Display all books
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

print("\n===== LIBRARY BOOK RECORDS =====")

for book in books:
    status = "Available" if book[3] else "Issued"

    print("Book ID:", book[0])
    print("Title:", book[1])
    print("Author:", book[2])
    print("Status:", status)
    print("-------------------------")

# Close the connection
connection.close()

print("Database operation completed successfully!")
