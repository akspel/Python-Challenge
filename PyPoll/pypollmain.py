import os
csvpath = os.path.join('Resources', 'election_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    next(csvreader)
    first_voter = next(csvreader)
    print(first_voter)

    total_votes = 0
    candidates_unique = []
    candidate_vote_count = []

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_in = (row[2])

        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

            print(f'Total votes: {total_votes}')
            print(f'Each candidate: {candidates_unique}')
            print(f'Index: {candidates_unique.index(candidate_in)}')

    pct = []
    max_votes = candidate_vote_count[0]
    max_index = 0

    for x in range(len(candidates_unique)):
        vote_pct = round(candidate_vote_count[x]/total_votes*100,2)
        pct.append(vote_pct)

        if candidate_vote_count[x] > max_votes:
            max_votes = candidate_vote_count[x]
            max_index = x
    election_winner = candidates_unique[max_index]

    print(f'Vote count for each candidate: {candidate_vote_count}')
    print(f'Max votes: {max_votes}')
    print(f'Election winner: {election_winner}')


# The total number of votes cast

# A complete list of candidates who recieved votes

# The percentage of votes each candidate won

# The number of votes each candidate won

# The winner of the election based on popular vote