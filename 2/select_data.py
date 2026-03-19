import sqlite3

DB_FILE = "company.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print("--- All employes ---")
cursor.execute("SELECT id, name, salary FROM employees")
for row in cursor.fetchall():
    print(f" ID={row[0]}  Name={row[1]:<8}  Salary={row[2]:,.0f} €")

print("\n --- Employes with salary over 70 000 € ---")    
cursor.execute("SELECT name, salary from employees WHERE salary > 70000")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]:,.0f} €")

print("\n--- EMployes sorted by salary from highest to lowest ---")
cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC")
for row in cursor.fetchall():
    print(f"  {row[0]:<8} {row[1]:,.0f} €")

print("\n--- Engineering employees hired after 2019, sorted by name ---")
cursor.execute("""SELECT name, salary, hire_date FROM employees 
                WHERE department_id = 1 AND hire_date > '2019-01-01' 
                ORDER BY name""")
for row in cursor.fetchall():
    print(f"  {row[0]:<8} {row[1]:,.0f} €  hired {row[2]}")

conn.close()

