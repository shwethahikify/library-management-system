import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get student ID
student_id = int(input("Enter Student ID: "))

# Retrieve student's book history
cursor.execute("""
SELECT issue_id, book_id, issue_date, return_date
FROM issued_books
WHERE student_id = ?
ORDER BY issue_id DESC
""", (student_id,))

records = cursor.fetchall()

print("\n===== STUDENT BOOK ISSUE HISTORY =====")

if records:
    for record in records:
        print("----------------------------")
        print("Issue ID:", record[0])
        print("Book ID:", record[1])
        print("Issue Date:", record[2])

        if record[3]:
            print("Return Date:", record[3])
            print("Status: Returned")
        else:
            print("Return Date: Not returned")
            print("Status: Currently Issued")

else:
    print("No book history found for this student.")

conn.close()
