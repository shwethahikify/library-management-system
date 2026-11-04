import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Display issued books
cursor.execute("""
SELECT issue_id, book_id, student_id, issue_date, return_date
FROM issued_books
""")

records = cursor.fetchall()

print("\n===== ISSUED BOOKS REPORT =====")

if records:
    for book in records:
        print("----------------------------")
        print("Issue ID:", book[0])
        print("Book ID:", book[1])
        print("Student ID:", book[2])
        print("Issue Date:", book[3])

        if book[4]:
            print("Return Date:", book[4])
            print("Status: Returned")
        else:
            print("Status: Not Returned")
else:
    print("No issued books found.")

conn.close()
