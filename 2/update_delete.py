import sqlite3

DB_FILE = "company.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def show_employees(label: str):
    print(f"\n--- {label} ---")
    cursor.execute("""
        SELECT      e.name, d.name, e.salary, e.hire_date
        FROM        employees e 
        JOIN        departments d ON e.department_id = d.id
        ORDER BY    e.name
                   """) 
    for row in cursor.fetchall():
        print(f"{row[0]:<8} | {row[1]:<15} | {row[2]:,.0f} €  | {row[3]}")

show_employees("Before any changes")


cursor.execute("UPDATE employees SET salary = salary * 1.10 WHERE name = 'Alice'")
conn.commit()
cursor.execute("SELECT salary FROM employees WHERE name = 'Alice'")
row = cursor.fetchone()
if row:
    print(f"\n Alice's new salary after 10% raise: {cursor.fetchone()[0]:,.0f} €")
else: 
    print("\n Alice not found")


cursor.execute("""
        UPDATE  employees
        SET     salary = salary * 1.05
        WHERE   department_id = (SELECT id FROM departments WHERE name = 'Engineering')
               """)
conn.commit()
print(f" 5% raise applied to {cursor.rowcount} Engineering employee(s)")

cursor.execute("UPDATE employees SET hire_date = '2018-01-15' WHERE name = 'Anne'")
conn.commit()
print("\n Anne's hire date updated")

cursor.execute("DELETE FROM employees WHERE name = 'Daniel'")
conn.commit()
print(f"\n Daniel deleted")

cursor.execute("SELECT COUNT(*) FROM employees")
remaining = cursor.fetchone()[0]
print(f"Employees remaining: {remaining}")

show_employees("After removing Daniel")

conn.close