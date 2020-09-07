import os
csvpath = os.path.join('Resources', 'budget_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    next(csvreader)
    first_month = next(csvreader)
    print(first_month)
    months = 0
    amount = int(first_month[1])
    for row in csvreader:
        months = months + 1
        amount = amount + int(row[1])
# calculating total months
    print(months)        