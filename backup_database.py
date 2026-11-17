import sqlite3
import os
from datetime import datetime

# Original database
database = "library.db"

# Check database exists
if os.path.exists(database):

    # Create backup filename
    backup_name = "library_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".db"

    # Create database backup
    source = sqlite3.connect(database)
    backup = sqlite3.connect(backup_name)

    source.backup(backup)

    source.close()
    backup.close()

    print("Database backup created successfully!")
    print("Backup file:", backup_name)

else:
    print("Library database not found!")
