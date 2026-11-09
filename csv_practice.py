import csv 
from datetime import datetime

SALES_FILE="sales.csv"
CLEANED_FILE="cleaned.csv"
LOG_FILE="run_log.txt"

print("-----Exercise 1 -----")
with open (SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE} for reading")

print("-----Exercise 2-----")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("-----Exercise 3-----")
with open(SALES_FILE, "r") as f:
    reader=csv.reader(f)
    header=next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)
print("-----Exercise 4-----")
total_revenue=0
with open(SALES_FILE, "r") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        product,price_str ,  qty_str = row
        price=float(price_str)
        quantity=int(qty_str)
        total=price*quantity
        total_revenue+=total
        print(f"{product}: {quantity} units x ${price} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

print("-----Exercise 5-----")

high_value=[]
rows_read=0


with open(SALES_FILE, "r") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            print(f"{product}: {quantity} units x ${price} = ${total:.2f}")
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open (CLEANED_FILE, "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["product", "price", "quantity", "total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}")

print("-----Exercise 6-----")
dict_total = 0

with open(SALES_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row['price'])
        quantity = int(row['quantity'])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price} = ${total:.2f}")
print(f"Total sales: ${dict_total:.2f}")


