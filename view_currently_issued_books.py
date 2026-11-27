import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Retrieve currently issued books
cursor.execute("""
    SELECT *
    FROM issued_books
    WHERE return_date IS NULL
""")

records = cursor.fetchall()

# Display records
if records:
    print("\n===== CURRENTLY ISSUED BOOKS =====")

    for record in records:
        print(record)

else:
    print("No books are currently issued.")

conn.close()
