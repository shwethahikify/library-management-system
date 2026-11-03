import sqlite3
from datetime import date

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Add return_date column if it does not exist
try:
    cursor.execute(
        "ALTER TABLE issued_books ADD COLUMN return_date TEXT"
    )
    conn.commit()
except sqlite3.OperationalError:
    pass

# Get details
book_id = int(input("Enter Book ID: "))
student_id = int(input("Enter Student ID: "))

# Find an active issued book
cursor.execute("""
SELECT issue_id FROM issued_books
WHERE book_id = ? AND student_id = ?
AND return_date IS NULL
ORDER BY issue_id DESC
LIMIT 1
""", (book_id, student_id))

record = cursor.fetchone()

if record:
    return_date = date.today().strftime("%Y-%m-%d")

    cursor.execute("""
    UPDATE issued_books
    SET return_date = ?
    WHERE issue_id = ?
    """, (return_date, record[0]))

    conn.commit()
    print("Book returned successfully!")
    print("Return Date:", return_date)
else:
    print("No active issued book found.")

conn.close()
