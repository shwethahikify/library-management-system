# Day 12: Library Management System
# Student Database using SQLite

import sqlite3

# Connect to database
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

def register_student():
    print("\n--- Student Registration ---")

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    department = input("Enter Department: ").strip()

    if not student_id or not name or not department:
        print("All fields are required!")
        return

    try:
        cursor.execute("""
        INSERT INTO students (student_id, name, department)
        VALUES (?, ?, ?)
        """, (student_id, name, department))

        connection.commit()
        print("Student registered successfully!")

    except sqlite3.IntegrityError:
        print("Student ID already exists!")

def display_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- Registered Students ---")

    if not records:
        print("No students registered yet.")
        return

    for student in records:
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Department:", student[2])
        print("--------------------")

while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting Student Database.")
        break
    else:
        print("Invalid choice!")

connection.close()
