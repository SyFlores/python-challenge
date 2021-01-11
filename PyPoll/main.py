import os
import csv

# Full file too large to upload to GitHub
# Alter the csv file path if you would like to run on a more complete data set
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
txtpath = os.path.join('..', 'PyPoll', 'election_results.txt')


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

    cand_dict = {cand_list[i]: {"Count" : 0, "Percentage" : 0} for i in range(0,len(cand_list))}

# Must rerun this in order to iterate back through the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    # Initiate variables to be used to determine and announce the winner
    winner = ""
    winner_count = 0

    for row in csvreader:
        # Every row, we check which candidate is getting which vote and incrementing their count
        for candidate in cand_list:
            if row[2] == candidate:
                cand_dict[candidate]["Count"] += 1

    # Calculating the percentage of votes each candidate has
    for candidate in cand_list:
        cand_dict[candidate]["Percentage"] = round((cand_dict[candidate]["Count"]*100)/vote_count,3)
        # Because we're already in this for loop, we can also determine which candidate has the highset number of votes
        if cand_dict[candidate]["Count"] > winner_count:
                winner_count = cand_dict[candidate]["Count"]
                winner = candidate

# Must initialize results2 as a string so it can be added to statement
results2 = ""

# Be sure to put closing quotes on a new line so next results show up there 
results1 = f"""Election Results
-------------------------
Total Votes: {vote_count}
-------------------------
"""

# Loop through candidates and output their indivual results
# These are then concatenated together
for candidate in cand_list:
    # Be sure to put closing quotes on a new line so next results show up there
    statement = (f"""{candidate}: {cand_dict[candidate]["Percentage"]}% ({cand_dict[candidate]["Count"]})
""")
    results2 += statement

results3 = f"""-------------------------
Winner: {winner}
-------------------------"""

# Join the three strings to get a single string - for easy export
election_results = results1 + results2 + results3

print(election_results)

# Create, export and close a text file with our analysis
text_file = open(txtpath, 'w+')
text_file.write(election_results)
text_file.close()
