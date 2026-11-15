import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Retrieve all student details
cursor.execute("""
SELECT * FROM students
""")

students = cursor.fetchall()

print("\n===== STUDENT DETAILS REPORT =====")

if students:
    for student in students:
        print("-----------------------------")
        print("Student ID:", student[0])
        print("Student Name:", student[1])
        print("Other Details:", student[2:])
else:
    print("No students registered.")

print("\nTotal Students:", len(students))

conn.close()
