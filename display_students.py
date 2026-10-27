import sqlite3

def display_students():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if students:
        print("\n--- Registered Students ---")

        for student in students:
            print("--------------------------")
            print("Student ID:", student[0])
            print("Student Name:", student[1])
            print("Department:", student[2])
            print("Phone Number:", student[3])
    else:
        print("No student records found.")

    conn.close()


display_students()
