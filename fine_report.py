import sqlite3
from datetime import date, datetime, timedelta

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get all issued book records
cursor.execute("""
SELECT issue_id, book_id, student_id, issue_date, return_date
FROM issued_books
""")

records = cursor.fetchall()

print("\n===== LIBRARY FINE REPORT =====")

if records:
    for record in records:
        issue_id, book_id, student_id, issue_date, return_date = record

        issued = datetime.strptime(
            issue_date, "%Y-%m-%d"
        ).date()

        due_date = issued + timedelta(days=14)

        if return_date:
            check_date = datetime.strptime(
                return_date, "%Y-%m-%d"
            ).date()
        else:
            check_date = date.today()

        late_days = max(0, (check_date - due_date).days)
        fine = late_days * 5

        print("----------------------------")
        print("Issue ID:", issue_id)
        print("Book ID:", book_id)
        print("Student ID:", student_id)
        print("Late Days:", late_days)
        print("Fine: Rs.", fine)

else:
    print("No issued books found.")

conn.close()
