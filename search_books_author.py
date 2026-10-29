import sqlite3

def search_books_by_author():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    author = input("Enter author name to search: ")

    cursor.execute(
        "SELECT * FROM books WHERE author LIKE ?",
        ('%' + author + '%',)
    )

    books = cursor.fetchall()

    if books:
        print("\n===== BOOKS BY AUTHOR =====")

        for book in books:
            print("--------------------------")
            print("Book ID:", book[0])
            print("Book Title:", book[1])
            print("Author:", book[2])
            print("Availability:", book[3])
    else:
        print("No books found for this author.")

    conn.close()


search_books_by_author()
