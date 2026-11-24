import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Count total books
cursor.execute("SELECT COUNT(*) FROM books")
total_books = cursor.fetchone()[0]

# Count currently issued books
cursor.execute("""
    SELECT COUNT(*)
    FROM issued_books
    WHERE return_date IS NULL
""")
issued_books = cursor.fetchone()[0]

# Calculate available books
available_books = total_books - issued_books

# Display statistics
print("===== BOOK STATISTICS =====")
print("Total Books:", total_books)
print("Issued Books:", issued_books)
print("Available Books:", available_books)
print("===========================")

conn.close()
