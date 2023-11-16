#dependencies
import os
import csv

#specify the path to collect data from
pybank_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyBank/Resources/budget_data.csv")

#read in the CSV file
with open(pybank_csv) as csvfile:
    #define csvreader variable, and split the columns at the commas in the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

# read the header row first
    csv_header = next(csvreader)
    #make the csv file into a list we can pull data from
    csv_list = list(csvreader)
    
# month list
month_list = [row[0] for row in csv_list]

#profit list turns the Profits/Losses column into integers we can work with later
profit_list = [int(row[1]) for row in csv_list]

# total months (calculated by using len to count the rows)
total_months = len(month_list)

# total profit
total_profit = sum(profit_list)

# list of profit changes within the range of months
profit_change = [profit_list[i] - profit_list[i-1] for i in range(1, total_months)]

month_change = [month_list[i] for i in range(1, total_months)]

average_change = sum(profit_change)/(total_months-1)

# find greatest increase in profits, and greatest decrease within the range. Define the date variables to correspond with the min/max profit rows
greatest_increase = max(profit_change)
for i in range(total_months-1):
    if profit_change[i]==greatest_increase:
        greatest_increase_date = month_change[i]
        
greatest_decrease = min(profit_change)
for i in range(total_months-1):
    if profit_change[i]==greatest_decrease:
        greatest_decrease_date = month_change[i]
        

#print output, making sure to round average change to 2 decimal points 
print("Financial Analysis")     
print("----------------------------")       
print(f"Total Months: "+ str(total_months))
print(f"Total: $" + str(total_profit))
print(f"Average Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_increase_date} (${greatest_decrease})")

# Specify the file path to write new file called "pybank_analysis.txt" into
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "pybank_analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents as textfile
with open(output_path, 'w') as textfile:
    # Write the txt 
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"{'Total: $'} {total_profit:,}\n")
    textfile.write(f"{'Average Change: '} ${round(average_change,2):,}\n")
    textfile.write(f"{'Greatest Increase in Profits: '} {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"{'Greatest Increase in Profits: '} {greatest_increase_date} (${greatest_decrease})\n")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     


