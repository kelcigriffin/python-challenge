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


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     # Read each row of data after the header
#for row in csvreader:
        #print(row)
