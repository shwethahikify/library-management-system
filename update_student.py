import sqlite3

def update_student():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    student_id = input("Enter Student ID to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        name = input("Enter new student name: ")
        department = input("Enter new department: ")
        phone = input("Enter new phone number: ")

        cursor.execute("""
            UPDATE students
            SET name = ?, department = ?, phone = ?
            WHERE student_id = ?
        """, (name, department, phone, student_id))

        conn.commit()
        print("Student details updated successfully!")

    else:
        print("Student not found!")

    conn.close()


update_student()
