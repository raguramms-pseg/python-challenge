# import the os module
import os

# import Module for reading CSV files
import csv

# set relative path to CSV file
csvpath = os.path.join(os.getcwd(),'Resources', 'election_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # Specify delimiter for CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    total_votes = 0
    #Declare a Dictionary to save key/Value pairs of candidates and their vote count
    candidates = {}

    # Read each row of data after the header an d accumulate vote count for each candidate and save in Dictionary
    for row in csvreader:

        if candidates.get(row[2]) == None:
            candidates[row[2]] = 0

        candidates[row[2]] = candidates[row[2]] + 1

        total_votes = total_votes + 1
        
    #open a text file to write results
    output = open(os.path.join(os.getcwd(),'analysis', 'analysis.txt'), 'w')
    
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(total_votes))
    print('-------------------------')

    output.write('Election Results\n')
    output.write('-------------------------\n')
    output.write('Total Votes: ' + str(total_votes) + '\n')
    output.write('-------------------------\n')

    winner = ''
    max_votes = 0

    #loop through candidates dictionary 
    for i in candidates:
        print(i + ': ' + str(round(100 * candidates[i] / total_votes, 3)) + '% (' + str(candidates[i]) + ')')
        output.write(i + ': ' + str(100 * round(candidates[i] / total_votes, 3)) + '% (' + str(candidates[i]) + ')\n')
        if winner == '' or candidates[i] > max_votes:
            winner = i
            max_votes = candidates[i]
    
    print('-------------------------')
    print('Winner: ' + winner)
    print('-------------------------')

    output.write('-------------------------\n')
    output.write('Winner: ' + winner + '\n')
    output.write('-------------------------\n')

    output.close()
