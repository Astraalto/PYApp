import sqlite3
import os


DB_FILE = "company.db"

if os.path.exists(DB_FILE):
    print(f"  'DB_FILE' already exists. Delete it first to start.")
    exit()

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE departments (
        id   INTEGER PRIMARY KEY,
        name TEXT NOT NULL      
               ) 
        """)

cursor.execute("""
    CREATE TABLE employees (
        id              INTEGER PRIMARY KEY,
        name            TEXT    NOT NULL, 
        department_id   INTEGER REFERENCES departments(id),
        salary          REAL    NOT NULL,
        hire_date       TEXT    NOT NULL                             
               )
        """)

conn.commit()
conn.close()

print(f" Database created: '{DB_FILE}'")
print("  Tables created: departemnts, employees")