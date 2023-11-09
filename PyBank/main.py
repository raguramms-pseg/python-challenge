# import the os module
import os

# import Module for reading CSV files
import csv

#path = os.getcwd()

#print(f"Current path is : {path} ")

csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join(os.getcwd(),'Resources', 'budget_data.csv')
print(f"Resources path is : {csvpath}")

# Read CSV file

with open(csvpath) as csvfile:
#
    # Specify delimiter for CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
