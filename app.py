import sqlite3

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    available INTEGER DEFAULT 1
)
""")

conn.commit()


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    cursor.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author)
    )
    conn.commit()
    print("Book added successfully!")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n--- Library Books ---")
    for book in books:
        status = "Available" if book[3] else "Issued"
        print(book[0], book[1], book[2], status)


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

conn.close()
