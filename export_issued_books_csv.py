import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Fetch issued book records
cursor.execute("SELECT * FROM issued_books")
records = cursor.fetchall()

# Get column names
columns = [description[0] for description in cursor.description]

# Export records to CSV
with open("issued_books_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(records)

print("Issued books report exported successfully!")

conn.close()
