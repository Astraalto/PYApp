import sqlite3

departments = [
    (1, "Engineering"),
    (2, "Marketing"),
    (3, "HR")
]

cursor.executemany("INSERT INTO departments VALUES (?,?)", departments)

employess = [
    (1, " Alice", 1, 75000, "2021-03-05"),
    (2, " Alice", 1, 82000, "2019-07-01"),
    (3, " Alice", 2, 61000, "2021-01-01"),
    (4, " Alice", 2, 55000, "2021-04-25"),
    (5, " Alice", 3, 58000, "2021-11-11"),
    (6, " Alice", 3, 91000, "2021-08-29")
]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employess)
conn.commit()
print(" Data inserted")