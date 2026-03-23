import os

DB_FILE = "company.db"

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"Database file deleted")
else:
    print(f"Database file not found")