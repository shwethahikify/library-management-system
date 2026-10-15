# Day 4: Library Management System
# Book Search Feature

books = [
    {"title": "Python Basics", "author": "John"},
    {"title": "Machine Learning", "author": "David"},
    {"title": "Artificial Intelligence", "author": "Smith"},
    {"title": "Data Structures", "author": "Robert"}
]

search = input("Enter book title or author: ").lower()

found = False

for book in books:
    if (search in book["title"].lower()
            or search in book["author"].lower()):
        print("Book Found!")
        print("Title:", book["title"])
        print("Author:", book["author"])
        found = True

if not found:
    print("Book not found!")
