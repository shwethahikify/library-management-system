import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get Book ID
book_id = input("Enter Book ID: ")

# Search issued book records
cursor.execute(
    "SELECT * FROM issued_books WHERE book_id = ?",
    (book_id,)
)

records = cursor.fetchall()

# Display results
if records:
    print("\n===== BOOK ISSUE HISTORY =====")

    for record in records:
        print(record)

else:
    print("No issue records found for this Book ID.")

conn.close()
