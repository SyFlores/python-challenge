import os
import csv



# Update this when you get your local repo syncing
# Doing this here to avoid accidentally deletin anything
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)

    unique_dates = []

    total_value = 0

    bank_date = []
    PandL = []
    PandL_Diff = []


    for row in csvreader:
        # Feed unique data values into a list
        if row[0] not in unique_dates:
            unique_dates.append(row[0])
        
        # Adding the individual values in the "Profit/Losses" column
        total_value += int(row[1])

        # Pulling values from the columns into lists
        bank_date.append(row[0])
        PandL.append(float(row[1]))

    # Using the above lists to create a dictionary for easy calculations and iteration
    budget = {"Date": bank_date, "Profit/Losses": PandL}

    # Looping through list to create a difference list
    for i in range(1, len(budget["Profit/Losses"])):
        PandL_Diff.append(budget["Profit/Losses"][i] - budget["Profit/Losses"][i-1])

    avg_PandL_Diff = sum(PandL_Diff)/len(PandL_Diff)
    
# Output - Data Summary
print(len(unique_dates))
print(total_value)
print(round(avg_PandL_Diff))
