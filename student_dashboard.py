import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get student ID
student_id = input("Enter Student ID: ")

# Find student details
cursor.execute(
    "SELECT * FROM students WHERE student_id = ?",
    (student_id,)
)

student = cursor.fetchone()

if student:
    print("\n===== STUDENT DASHBOARD =====")
    print("Student Details:", student)

    # Count total borrowed books
    cursor.execute("""
    SELECT COUNT(*) FROM issued_books
    WHERE student_id = ?
    """, (student_id,))

    total_books = cursor.fetchone()[0]

    # Count currently issued books
    cursor.execute("""
    SELECT COUNT(*) FROM issued_books
    WHERE student_id = ? AND return_date IS NULL
    """, (student_id,))

    active_books = cursor.fetchone()[0]

    print("Total Books Borrowed:", total_books)
    print("Currently Issued Books:", active_books)
    print("Returned Books:", total_books - active_books)

else:
    print("Student not found!")

conn.close()
