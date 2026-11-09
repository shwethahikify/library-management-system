import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get book ID
book_id = int(input("Enter Book ID: "))

# Check whether the book is already issued
cursor.execute("""
SELECT issue_id
FROM issued_books
WHERE book_id = ? AND return_date IS NULL
""", (book_id,))

record = cursor.fetchone()

if record:
    print("Sorry! This book is already issued.")
    print("Please select another book.")

else:
    print("This book is available for issuing.")

conn.close()
