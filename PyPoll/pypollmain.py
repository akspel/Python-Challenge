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
# A complete list of candidates who recieved votes
    print(f'Each Candidates: {candidates_unique}')                         

# define more variables
    pct = []
    max_votes = candidates_vote_count[0]
    max_index = 0

 # create another loop
    for x in range(len(candidates_unique)):
        vote_pct = round(candidates_vote_count[x]/total_votes*100, 2)
        pct.append(vote_pct)

        if candidates_vote_count[x] > max_votes:
            max_votes = candidates_vote_count[x]
            max_index = x
    election_winner = candidates_unique[max_index]
           
#  The number of votes each candidate won
    print(f'Votes for each Candidate: {candidates_vote_count}')
# The winner of the election based on the popular vote
    print(f'Max Votes: {max_votes}')
    print(f'Election Winner: {election_winner}')
# The percentage of votes each candidate won
    for x in range(len(candidates_unique)):
        print(f'{candidates_unique[x]} : {pct[x]}% ({candidates_vote_count[x]})')



                







