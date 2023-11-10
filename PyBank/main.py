# import the os module
import os

# import Module for reading CSV files
import csv

# set relative path to CSV file
csvpath = os.path.join(os.getcwd(),'Resources', 'budget_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # Specify delimiter for CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    total_months = 0
    net_total_amount = 0
    greatest_increase_profit_amount = 0
    greatest_increase_profit_date = ''
    greatest_decrease_profit_amount = 0
    greatest_decrease_profit_date = ''
    last = 0
    average_change = 0

    # Read each row of data after the header and accumulate totals
    for row in csvreader:

        if(total_months == 0):
            greatest_increase_profit_date = row[0]
            greatest_increase_profit_amount = int(row[1])
            greatest_decrease_profit_date = row[0]
            greatest_decrease_profit_amount = int(row[1])

        else:
            average_change += int(row[1]) - last
            if(int(row[1]) - last > greatest_increase_profit_amount):
                greatest_increase_profit_amount = int(row[1]) - last
                greatest_increase_profit_date = row[0]

            if(int(row[1]) - last < greatest_decrease_profit_amount):
                greatest_decrease_profit_amount = int(row[1]) - last
                greatest_decrease_profit_date = row[0]

        total_months = total_months + 1
        net_total_amount = net_total_amount + int(row[1])

        last = int(row[1])
        
    
    average_change = round(average_change / (total_months - 1), 2)

    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(net_total_amount))
    print('Average Change: $' + str(average_change))
    print('Greatest Increase in Profits: ' + str(greatest_increase_profit_date) + ' ($' + str(greatest_increase_profit_amount) + ')')
    print('Greatest Decrease in Profits: ' + str(greatest_decrease_profit_date) + ' ($' + str(greatest_decrease_profit_amount) + ')')

    #open a text file to write results
    output = open(os.path.join(os.getcwd(),'analysis', 'analysis.txt'), 'w')
    output.write('Financial Analysis\n')
    output.write('----------------------------\n')
    output.write('Total Months: ' + str(total_months) + '\n')
    output.write('Total: $' + str(net_total_amount) + '\n')
    output.write('Average Change: $' + str(average_change) + '\n')
    output.write('Greatest Increase in Profits: ' + str(greatest_increase_profit_date) + ' ($' + str(greatest_increase_profit_amount) + ')\n')
    output.write('Greatest Decrease in Profits: ' + str(greatest_decrease_profit_date) + ' ($' + str(greatest_decrease_profit_amount) + ')\n')
    output.close()
