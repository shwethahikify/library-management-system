import sqlite3
from datetime import date, datetime, timedelta

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Get issue ID
issue_id = int(input("Enter Issue ID: "))

# Find issue details
cursor.execute("""
SELECT issue_date, return_date
FROM issued_books
WHERE issue_id = ?
""", (issue_id,))

record = cursor.fetchone()

if record:
    issue_date = datetime.strptime(
        record[0], "%Y-%m-%d"
    ).date()

    if record[1]:
        check_date = datetime.strptime(
            record[1], "%Y-%m-%d"
        ).date()
    else:
        check_date = date.today()

    due_date = issue_date + timedelta(days=14)
    late_days = max(0, (check_date - due_date).days)

    fine = late_days * 5

    print("\n===== LIBRARY FINE REPORT =====")
    print("Issue Date:", issue_date)
    print("Due Date:", due_date)
    print("Late Days:", late_days)
    print("Total Fine: Rs.", fine)

else:
    print("Invalid Issue ID.")

conn.close()
