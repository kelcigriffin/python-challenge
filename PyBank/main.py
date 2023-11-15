import os
import csv

pybank_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyBank/Resources/budget_data.csv")


with open(pybank_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
        next(csvreader)
        row = next(csvreader)
        current_amt = int(row[1])
        first_amt = net_total = current_amt
        previous_amt = current_amt

        row = next(csvreader)
        total_months = 2
        current_amt = int(row[1])
        net_total= net_total + current_amt
        amt_diff = current_amt - previous_amt
        max_incr = max_decr = amt_diff
        max_incr_date = max_decr_date = row[0]
        previous_amt = current_amt

        for row in csvreader:
            total_months = total_months + 1
            current_amt = int(row[1])
            net_total= net_total + current_amt
            amt_diff = current_amt - previous_amt

            if amt_diff > max_incr:
                  max_incr = amt_diff
                  max_incr_date = row[0]

            if amt_diff < max_decr:
                 max_decr = amt_diff
                 max_decr_date = row[0]
            previous_amt = current_amt
            
average_change = (current_amt - first_amt) / (total_months - 1)



print("Financial Analysis")     
print("----------------------------")       
print(f"Total Months: "+ str(total_months))
print(f"Total: $" + str(net_total))
print(f"Average Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: {max_incr_date} (${max_incr})")
print(f"Greatest Decrease in Profits: {max_decr_date} (${max_decr})")


# report = (
#     f"{' Financial Analysis ':-^48}\n"
#     f"{'Total Months:':24}{total_months:24,.0f}\n"
#     f"{'Net Profits:':24}{net_total:24,.0f}\n"
#     f"{'Avg Change:':24}{average_change:24,.2f}\n"
#     f"{'Max Increase:':14}{max_incr[0]:^20}{max_incr[1]:14,.0f}\n"
#     f"{'Max Decrease:':14}{max_decr[0]:^20}{max_decr[1]:14,.0f}\n"
#     f"{'--':-^48}"
# )
# Specify the file to write to
output_path = os.path.join(os.path.dirname(__file__), "Analysis", "pybank_analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    
    # Write the first row (column headers)
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    # Write the second row
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"{'Total: $'} {net_total:,}\n")
    textfile.write(f"{'Average Change: '} ${round(average_change,2):,}\n")
    textfile.write(f"{'Greatest Increase in Profits: '} {max_incr_date} (${max_incr:,})\n")
    textfile.write(f"{'Greatest Increase in Profits: '} {max_decr_date} (${max_decr:,})\n")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     # Read each row of data after the header
#for row in csvreader:
        #print(row)





