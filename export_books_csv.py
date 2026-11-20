import sqlite3
import csv

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Retrieve book records
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

# Get column names
columns = [description[0] for description in cursor.description]

# Export records to CSV
with open("books_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(books)

print("Books exported successfully!")
print("File created: books_report.csv")

conn.close()
