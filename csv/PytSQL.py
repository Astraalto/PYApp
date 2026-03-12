import sqlite3

conn = sqlite3.connect("myynti.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXIST myynti (
               asiakas TEXT,
               määrä INTEGER
               )
               """)

cursor.exexute("INSERT INTO myynti VALUES ('Sanna', 130)")
cursor.exexute("INSERT INTO myynti VALUES ('Jukka', 90)")

conn.comit()

cursor.execute("""
    SELECT asiakas, SUM(määrä)
    FROM myynti
    GROUP BY asiakas              
        """)

rows = cursor.fetchall()

for row in rows:
    print(row)
