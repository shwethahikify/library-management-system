import sqlite3

def connect_database():
    return sqlite3.connect("library.db")


def display_books():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n===== BOOK DETAILS =====")

    for book in books:
        print(book)

    if not books:
        print("No books found.")

    conn.close()


def display_students():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n===== STUDENT DETAILS =====")

    for student in students:
        print(student)

    if not students:
        print("No students found.")

    conn.close()


def count_books():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    print("Total Books:", cursor.fetchone()[0])

    conn.close()


def count_students():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    print("Total Students:", cursor.fetchone()[0])

    conn.close()


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Display Students")
    print("3. Count Books")
    print("4. Count Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        display_students()

    elif choice == "3":
        count_books()

    elif choice == "4":
        count_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
