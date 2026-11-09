import csv 
from datetime import datetime

SALES_FILE="sales.csv"
CLEANED_FILE="data/cleaned.csv"
LOG_FILE="data/run_log.txt"

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