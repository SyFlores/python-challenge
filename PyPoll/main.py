import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data_full.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    vote_count = 0

    # Read each row of data after the header
    for row in csvreader:
        vote_count += 1

print(str(vote_count))
