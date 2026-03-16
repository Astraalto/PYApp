import sqlite3

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

print("\n Tables created: departments, employees")