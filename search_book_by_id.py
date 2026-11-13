import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get Book ID
book_id = input("Enter Book ID: ")

# Search book details
cursor.execute("""
SELECT * FROM books
WHERE book_id = ?
""", (book_id,))

book = cursor.fetchone()

print("\n===== BOOK SEARCH RESULT =====")

if book:
    print("Book ID:", book[0])
    print("Book Title:", book[1])
    print("Author:", book[2])
    print("Book Details:", book)
else:
    print("Book not found!")

conn.close()
