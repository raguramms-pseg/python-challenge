# python-challenge
Module-3 Python Assignment

PyBank Module
-------------

Python script main.py analyzes the financial records of a company. The script reads csv file budget_data.csv located in resources folder. 

CSV file contains 2 columns : "Date" and "Profit/Losses".
Script loos through all rows to calculate each of the following values:

The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

The results are written to a text file - analysis.txt located in analysis folder

PyPoll Module
-------------

Python script main.py analyzes the election results. The script reads a csv file - election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

A dictoinary is defined to store unique candidates and the count of votes casted in their favor. 

The script loops thru the rows in csv file and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

The results are written to a text file - analysis.txt located in analysis folder
