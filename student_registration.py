# Day 6: Library Management System
# Student Registration Feature

students = []

def register_student():
    print("\n--- Student Registration ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    student = {
        "id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)
    print("Student registered successfully!")

def display_students():
    print("\n--- Registered Students ---")

    if not students:
        print("No students registered yet.")
        return

    for student in students:
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("--------------------")

while True:
    print("\n===== Library Management System =====")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
