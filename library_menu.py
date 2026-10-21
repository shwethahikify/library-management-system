# Day 10: Library Management System
# Library Main Menu

books = [
    {"id": 101, "title": "Python Basics", "available": True},
    {"id": 102, "title": "Machine Learning", "available": True},
    {"id": 103, "title": "Artificial Intelligence", "available": True}
]

students = []

def display_books():
    print("\n--- Book List ---")
    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(book["id"], "-", book["title"], "-", status)

def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    students.append({"id": student_id, "name": name})
    print("Student registered successfully!")

def issue_book():
    try:
        book_id = int(input("Enter Book ID to issue: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found!")

def return_book():
    try:
        book_id = int(input("Enter Book ID to return: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book has not been issued.")
            return

    print("Book not found!")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Register Student")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()
    elif choice == "2":
        register_student()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
