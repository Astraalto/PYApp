import csv

sales_per_period = {}

with open("csv/business2025.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        period = row["Period"]
        amount_str = row["Data_value"].strip()
        if not amount_str:
            continue
        amount = float(row["Data_value"])

        if period not in sales_per_period:
            sales_per_period[period] = 0

        sales_per_period[period] += amount

for time, total in sales_per_period.items():
    print(time, total)
