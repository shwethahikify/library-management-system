# Day 13: Library Management System
# Search Student using SQLite

import sqlite3

# Connect to the database
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Create students table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

connection.commit()

def search_student():
    student_id = input("Enter Student ID to search: ").strip()

    if not student_id:
        print("Please enter a Student ID.")
        return

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\n--- Student Found ---")
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Department:", student[2])
    else:
        print("Student not found!")

while True:
    print("\n===== SEARCH STUDENT =====")
    print("1. Search Student")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_student()
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

connection.close()
