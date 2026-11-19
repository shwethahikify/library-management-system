import sqlite3
import os

# Enter backup filename
backup_file = input("Enter backup database filename: ")

# Check whether backup exists
if os.path.exists(backup_file):

    try:
        # Connect to backup and original database
        backup = sqlite3.connect(backup_file)
        original = sqlite3.connect("library.db")

        # Restore database
        backup.backup(original)

        backup.close()
        original.close()

        print("Database restored successfully!")

    except sqlite3.Error as error:
        print("Database restore failed:", error)

else:
    print("Backup file not found!")
