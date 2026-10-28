import sqlite3

def display_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if books:
        print("\n===== LIBRARY BOOK LIST =====")

        for book in books:
            print("-----------------------------")
            print("Book ID:", book[0])
            print("Book Title:", book[1])
            print("Author:", book[2])
            print("Availability:", book[3])
    else:
        print("No books found in the library.")

    conn.close()


display_books()
