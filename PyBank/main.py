import os
csvpath = os.path.join('Resources', 'budget_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)
def print_budget(budget_data):
    date = str(budget_data[0])
    budget = int(budget_data[1])

    total_months = date
    

