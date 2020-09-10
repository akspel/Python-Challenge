# import and read csv file
import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    first_voter = next(csvreader)
    print(first_voter)
    