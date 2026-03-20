import sqlite3

DB_FILE = "company.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print("--- Overall salary ---")
cursor.execute("""
                    SELECT 
                        COUNT(*)                AS number_of_employees, 
                        ROUND(AVG(salary), 0)   AS avg_salary, 
                        MIN(salary)             AS min_salary,
                        MAX(salary)             AS max_salary,
                        SUM(salary)             AS total_amount  
                    FROM employees
                """)

row = cursor.fetchone()
print(f" Number of employees : {row[0]}")
print(f" Average salary : {row[1]:,.0f} €")
print(f" Minimum salary: {row[2]:,.0f} €")
print(f" Maximum salary : {row[3]:,.0f} €")
print(f" Total amount : {row[4]:,.0f} €")

print("\n--- Number of employees and avaerage salry per department ---")
cursor.execute("""
                    SELECT 
                        department_id,
                        COUNT(*)                AS number_of_employees, 
                        ROUND(AVG(salary), 0)   AS avg_salary
                    FROM employees
                    GROUP BY department_id
                    ORDER BY avg_salary DESC
                """)
for row in cursor.fetchall():
    print(f" Department  {row[0]}  |  {row[1]} employees  |  average salary {row[2]:,.0f} €")

print("\n--- Number of departments with more thant 1 employee ---")
cursor.execute("""
                    SELECT          department_id, COUNT(*) AS number_of_employees
                    FROM            employees
                    GROUP BY        department_id
                    HAVING          number_of_employees > 1 
                """)

for row in cursor.fetchall():
    print(f" Department {row[0]} |  {row[1]} employees")

conn.close()