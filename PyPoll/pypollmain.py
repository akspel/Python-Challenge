# import and read csv file
import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    first_voter = next(csvreader)
    print(first_voter)

 # define variables
    total_votes = 1
    candidates_unique = []
    candidates_vote_count = []

 # create for loop
    for row in csvreader:
        total_votes = total_votes + 1




 # The total numbers of votes cast
        print(total_votes)             