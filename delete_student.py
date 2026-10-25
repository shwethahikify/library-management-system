import sqlite3

def delete_student():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    student_id = input("Enter Student ID to delete: ")

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
        )

        if confirm.lower() == "yes":
            cursor.execute(
                "DELETE FROM students WHERE student_id = ?",
                (student_id,)
            )
            conn.commit()
            print("Student record deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found!")

    conn.close()


delete_student()
