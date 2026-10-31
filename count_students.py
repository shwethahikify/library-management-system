import sqlite3

def count_students():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    print("\n===== STUDENT REPORT =====")
    print("Total Registered Students:", total_students)

    conn.close()


count_students()
