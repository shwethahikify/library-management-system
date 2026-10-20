# Day 9: Library Management System
# Librarian Login System

USERNAME = "librarian"
PASSWORD = "lib123"

def librarian_login():
    print("\n===== LIBRARIAN LOGIN =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        print("Welcome to the Library Management System.")
    else:
        print("Invalid username or password!")

librarian_login()
