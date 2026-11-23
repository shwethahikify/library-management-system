import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Count total books
cursor.execute("SELECT COUNT(*) FROM books")
total_books = cursor.fetchone()[0]

# Count total students
cursor.execute("SELECT COUNT(*) FROM students")
total_students = cursor.fetchone()[0]

# Count issued books
cursor.execute("SELECT COUNT(*) FROM issued_books")
total_issued = cursor.fetchone()[0]

# Display library summary
print("===== LIBRARY SUMMARY REPORT =====")
print("Total Books:", total_books)
print("Total Students:", total_students)
print("Total Issued Books:", total_issued)
print("==================================")

conn.close()
