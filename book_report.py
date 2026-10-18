# Day 7: Library Management System
# Book Availability Report

books = [
    {"id": 101, "title": "Python Basics", "author": "John", "available": True},
    {"id": 102, "title": "Machine Learning", "author": "David", "available": False},
    {"id": 103, "title": "Artificial Intelligence", "author": "Smith", "available": True},
    {"id": 104, "title": "Data Structures", "author": "Robert", "available": False},
    {"id": 105, "title": "Database Management", "author": "James", "available": True}
]

def display_report():
    print("\n===== BOOK AVAILABILITY REPORT =====")

    available_count = 0
    issued_count = 0

    for book in books:
        if book["available"]:
            status = "Available"
            available_count += 1
        else:
            status = "Issued"
            issued_count += 1

        print("Book ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)
        print("------------------------------")

    print("Total Books:", len(books))
    print("Available Books:", available_count)
    print("Issued Books:", issued_count)

display_report()
