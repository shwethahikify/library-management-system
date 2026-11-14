import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get student name
name = input("Enter Student Name: ")

# Search student details
cursor.execute("""
SELECT * FROM students
WHERE name LIKE ?
""", ('%' + name + '%',))

students = cursor.fetchall()

print("\n===== STUDENT SEARCH RESULTS =====")

if students:
    for student in students:
        print("-------------------------")
        print("Student Details:", student)
else:
    print("Student not found!")

conn.close()
