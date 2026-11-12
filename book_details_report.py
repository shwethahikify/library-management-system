import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Retrieve all book details
cursor.execute("SELECT * FROM books")

books = cursor.fetchall()

print("\n===== LIBRARY BOOK DETAILS REPORT =====")

if books:
    for book in books:
        print("-----------------------------")
        print("Book ID:", book[0])
        print("Book Title:", book[1])
        print("Author:", book[2])

else:
    print("No books found in the library.")

print("\nTotal Books:", len(books))

conn.close()
