import csv
"""
with open("csv/business2025.csv") as file:
        reader = csv.DictReader(file)

        total = 0
        for row in reader:
            total += float(row["Data_value"])

        print("Total value:", total) 
"""

total = 0

with open("csv/Testi.csv") as file:
    reader =csv.DictReader(file)

    for row in reader:
        total += int(row["määrä"])

print("Totaali myynti:", total)
