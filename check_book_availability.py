import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get book ID
book_id = int(input("Enter Book ID: "))

# Check book details
cursor.execute("""
SELECT book_id, title
FROM books
WHERE book_id = ?
""", (book_id,))

book = cursor.fetchone()

if book:
    # Check whether the book is currently issued
    cursor.execute("""
    SELECT issue_id
    FROM issued_books
    WHERE book_id = ? AND return_date IS NULL
    """, (book_id,))

    issued = cursor.fetchone()

    print("\nBook Name:", book[1])

    if issued:
        print("Status: Book is currently issued.")
    else:
        print("Status: Book is available.")

else:
    print("Book not found.")

conn.close()
