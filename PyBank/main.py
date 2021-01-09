import os
import csv



# Update this when you get your local repo syncing
# Doing this here to avoid accidentally deletin anything
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)