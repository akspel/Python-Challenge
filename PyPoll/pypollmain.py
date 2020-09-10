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
        candidate_in = (row[2])

        # finding the different candidates
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidates_vote_count[candidate_index] = candidates_vote_count[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidates_vote_count.append(1)   



 # The total numbers of votes cast
        print(f'Total Votes: {total_votes}')
 # A complete list of the candidates who recieved votes
        print(f'Each Candidate: {candidate_in}')

