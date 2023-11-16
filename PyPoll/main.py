import os
import csv


pypoll_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyPoll/Resources/election_data.csv")


with open(pypoll_csv) as csvfile:

#     
        csvreader = csv.reader(csvfile, delimiter=',')
        row = next(csvreader)
        
        csv_list = list(csvreader)

votes = [row[2] for row in csv_list]
total_votes = (len(votes))

tallies = []
names = []

for name in votes:
    if name not in names:
        names.append(name)
        tallies.append(0)


for vote in votes:
     for i, name in enumerate(names):
        if vote == name:
             tallies[i] +=1 


for i, name in enumerate(names):

    most = max(tallies)


for i, vote in enumerate(tallies):
    if vote == most:
        winner = names[i]


print(f"Election Results\n")
print(f"-------------------------\n")
print(f"Total Votes:  {total_votes}\n")
print(f"-------------------------\n")

for i, name in enumerate(names):
    print(f"{name:<24}  {(tallies[i]/total_votes)*100:5,.2f}% ({tallies[i]:7,}) \n")             

       
print(f"-------------------------\n")
print(f"Winner: {winner}\n")
print(f"-------------------------\n")

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









