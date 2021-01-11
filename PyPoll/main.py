import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data_full.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    vote_count = 0

    cand_list = []

    # Read each row of data after the header
    for row in csvreader:
        # Quick incr for vote count
        vote_count += 1

        # Feed unique candidates into a list
        if row[2] not in cand_list:
            cand_list.append(row[2])

print(str(vote_count))
print(cand_list)
