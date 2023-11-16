# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#------------------------------------------------------------------------------
#dependencies
import os
import csv

#specify the path to collect data from
pypoll_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyPoll/Resources/election_data.csv")

#read in the CSV file
with open(pypoll_csv) as csvfile:

    #define csvreader variable, and split the columns at the commas in the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    #read header row, and move to next row
    row = next(csvreader)
    #make the csv file into a list we can pull data from   
    csv_list = list(csvreader)
#count the number of rows after the header, to calculate the amt of votes. I just set it to look at the Candidate column, 
# because I'm counting votes for candidates
votes = [row[2] for row in csv_list]
total_votes = (len(votes))

#start list of tallies and names, so I can store info for each candidate's name and their vote tallies
tallies = []
names = []

#for each name in the candidates column, if the name is unique from the one above it, add it to the list. Additionally,
# record a tally. Tally count starts at 0
for name in votes:
    if name not in names:
        names.append(name)
        tallies.append(0)

#count how many times each name is repeated, record the total for each candidate's name
for vote in votes:
     for i, name in enumerate(names):
        if vote == name:
             tallies[i] +=1 

#identify which name has received the most votes
for i, name in enumerate(names):

    most = max(tallies)

#if a candidate's name appears the most, they are the winner!
for i, vote in enumerate(tallies):
    if vote == most:
        winner = names[i]

#print output
print(f"Election Results\n")
print(f"-------------------------\n")
print(f"Total Votes:  {total_votes}\n")
print(f"-------------------------\n")

for i, name in enumerate(names):
    print(f"{name:<24}  {(tallies[i]/total_votes)*100:5,.2f}% ({tallies[i]:7,}) \n")             

       
print(f"-------------------------\n")
print(f"Winner: {winner}\n")
print(f"-------------------------\n")

#begin txt output
# Specify the file to write to
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "election_analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    
    # Write the first row (column headers)
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes:  {total_votes}\n")
    textfile.write(f"-------------------------\n")

    for i, name in enumerate(names):
        textfile.write(f"{name:<24}  {(tallies[i]/total_votes)*100:5,.2f}% ({tallies[i]:7,})\n")             

       
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winner}\n")                       
    textfile.write(f"-------------------------\n")









