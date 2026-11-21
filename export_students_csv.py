import sqlite3
import csv

# Connect to the library database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Fetch all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

# Get column names automatically
columns = [description[0] for description in cursor.description]

# Export records to CSV
with open("students_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(students)

print("Student records exported successfully!")

conn.close()
