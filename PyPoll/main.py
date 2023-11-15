import os
import csv


pypoll_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyPoll/Resources/election_data.csv")
#total_votes = 0

with open(pypoll_csv) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
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
        #print(names,tallies)

#for i, name in enumerate(names):
     #print(i, name, names[i])

for vote in votes:
     for i, name in enumerate(names):
        if vote == name:
             tallies[i] +=1 


for i, name in enumerate(names):
     #print(name, tallies[i])

    most = max(tallies)
#print(most)

for i, vote in enumerate(tallies):
    if vote == most:
        winner = names[i]

#print(winner, most)
print(f"Election Results\n")
print(f"-------------------------\n")
print(f"Total Votes:  {total_votes}\n")
print(f"-------------------------\n")

for i, name in enumerate(names):
    print(f"{name:<24} {tallies[i]:8,}   {(tallies[i]/total_votes)*100:5,.2f}%\n")             

       
print(f"-------------------------\n")
print(f"Winner: {winner}")
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
        textfile.write(f"{name:<24} {tallies[i]:8,}   {(tallies[i]/total_votes)*100:5,.2f}%\n")             

       
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"-------------------------\n")



# # Format the votes dictionary entries for the report
# lines = [
#     f"{k + ':':24}" f"{votes[k]:10,}" f"{votes[k]/total * 100:11,.2f}%\n"
#     for k in sorted(votes)
# ]
# # Generate the report string text
# report = (
#     f"{' Election Results ':^46}\n"
#     f"{'--':-^46}\n"
#     f"{'Total Votes:':24}{total:10,}{100:11,.2f}%\n"
#     f"{'--':-^46}\n"
#     f"{''.join(lines)}"
#     f"{'--':-^46}\n"
#     f"{'Winner:':10}{winner:>24}{votes[winner]/total * 100:11,.2f}%\n"
#     f"{'--':-^46}\n"
# )
