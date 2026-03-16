import sqlite3


conn = sqlite3.connect(":memory")
cursor = conn.cursor()

print("=" * 50)
print("DATABASE CREATED")