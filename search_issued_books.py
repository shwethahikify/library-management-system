import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get Student ID
student_id = input("Enter Student ID: ")

# Search issued books
cursor.execute(
    "SELECT * FROM issued_books WHERE student_id = ?",
    (student_id,)
)

records = cursor.fetchall()

# Display results
if records:
    print("\n===== ISSUED BOOK DETAILS =====")

    for record in records:
        print(record)

else:
    print("No issued books found for this Student ID.")

conn.close()
