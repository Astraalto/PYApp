import sqlite3

DB_FILE = "company.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print("--- Employee list with department names (INNER JOIN) ---")
cursor.execute("""
    SELECT
            e.name          as employee,
            d.name          as department,
            e.salary,
            e.hire_date
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    ORDER BY e.name
               """)
for row in cursor.fetchall():
    print(f" {row[0]:<8}    |   {row[1]:<15}     |   {row[2]:,.0f} €   |   {row[3]} ")


print("\n--- Engineering employees sorted by salary ---")
cursor.execute("""
    SELECT  e.name, e.salary, e.hire_date
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    WHERE d.name = 'Engineering'
    ORDER BY e.salary DESC
               """)
for row in cursor.fetchall():
    print(f"  {row[0]:<8} {row[1]:,.0f} €  hired {row[2]}")

print("\n--- Average salary per department (with names) ---")
cursor.execute("""
    SELECT
            d.name                  as department,
            COUNT(e.id)             as number_of_employees,
            ROUND(AVG(e.salary))    as avg_salary,
            SUM(e.salary)           as total_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    GROUP BY d.name
    ORDER BY 3 DESC   
               """)
for row in cursor.fetchall():
    print(f"  {row[0]:<15} | {row[1]} people | avg {row[2]:,.0f} € | total {row[3]:,.0f} €")

print("\n--- All departments, even if empty (LEFT JOIN) ---")
cursor.execute("INSERT INTO departments VALUES (4, 'Legal')")

cursor.execute("""
    SELECT
            d.name                  as department,
            COUNT(e.id)             as number_of_employees
    FROM    departments d
    LEFT JOIN employees e ON e.department_id = d.id
    GROUP BY d.name
    ORDER BY number_of_employees DESC     
               """)
for row in cursor.fetchall():
    status = "No staff" if row[1] == 0 else f"{row[1]} employee(s)"
    print(f"    {row[0]:<15} {status}")

conn.close()