# Day 5: Library Management System
# Book Issue and Return Feature

books = [
    {"title": "Python Basics", "available": True},
    {"title": "Machine Learning", "available": True},
    {"title": "Artificial Intelligence", "available": True}
]

def display_books():
    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print("-", book["title"])

def issue_book():
    title = input("Enter book title to issue: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully!")
            else:
                print("Sorry, this book is already issued.")
            return

    print("Book not found!")

def return_book():
    title = input("Enter book title to return: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return

    print("Book not found!")

while True:
    print("\n--- Library Management System ---")
    print("1. Display Available Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
