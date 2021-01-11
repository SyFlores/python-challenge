### Sources
- How to convert a list into a dictionary
  - The best way I could think of to naturally refer to nested values (apart from creating an array) is with a dictionary
  - Used the guts in a function I found as a guide for the template I wanted to create
    - Source: [Method #1](https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/)

### Collaborations
- No collaborations

### Thoughts
- What is being asked?
  - Calculate the number of votes
    - We might want to check if all rows are votes
    - It appears that all rows are votes
  - A complete list of candidates that received votes
    - We need a unique list, checking through every row
  - Percentage and number of votes for each candidate
- Pseudocode
  - Return a list of candidates from the 'for row in csvreader' loop
  - Use that list to run conditionals in a loop to update count variables for each
  - Use a loop to autocreate a dictionary
  - Results should also be printed from a loop
  - Once you iterate through a csvrader, you will have to create a separate with open() statement
    - Ran into a lot of headaches trying to iterate throught the csv multiple times
    - Necessary because we needed to iterate through once to get the unique candidates and convert list into a dictionary once done
  - Since the middle part of the output is needs a for loop to read, we can stitch together different parts of the output together
    - Be mindful of how the triple-quotes f-string treats new lines, in order to get the exact format
    - Stitching everything together into one variable will make the export process much easier.
