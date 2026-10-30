import sqlite3

def count_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    print("\n===== LIBRARY BOOK REPORT =====")
    print("Total number of books:", total_books)

    conn.close()


count_books()
