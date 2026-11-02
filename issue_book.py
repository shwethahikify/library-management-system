import sqlite3
from datetime import date

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create issue table
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    student_id INTEGER,
    issue_date TEXT
)
""")

# Get details
book_id = int(input("Enter Book ID: "))
student_id = int(input("Enter Student ID: "))

# Issue book
issue_date = date.today().strftime("%Y-%m-%d")

cursor.execute("""
INSERT INTO issued_books (book_id, student_id, issue_date)
VALUES (?, ?, ?)
""", (book_id, student_id, issue_date))

conn.commit()

print("Book issued successfully!")
print("Issue Date:", issue_date)

conn.close()
