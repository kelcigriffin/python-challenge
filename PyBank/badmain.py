import os
import csv

#py_bank_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyBank/Resources/budget_data.csv")

# total_months = []
# profit = []
# monthly_changes = []

# net_total = 0
# total_change = 0
# initial_profit = 0
# count = 0




# with open(py_bank_csv) as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
#         csvreader = csv.reader(csvfile, delimiter=',')

#         #print(csvreader)

#     # Read the header row first (skip this step if there is no header)
#         csv_header = next(csvreader)
#         row = next(csvreader)
            
#         for row in csvreader:
#             count = count+1
#             month = (row [0])
#             total_months.append(month)
#             current_amt = int(row[1])
#             net_total = net_total + current_amt
#             final_profit = int(row[1])
#             monthly_change = final_profit - initial_profit
#             monthly_changes.append(monthly_change)
#             total_change = total_change + monthly_change
#             #average_change = ((final_profit-initial_profit)/count-1)
#             initial_profit = final_profit
#             greatest_increase = max(monthly_changes)
#             greatest_decrease = min(monthly_changes) 
#             #column1 = {"Profits/Losses": (row[1])}
#             last_value = int((row[1])) 
#             average_change = ((final_profit-1088983))

#         #for i in csvreader:
#             #first_value = int(i[1])
#          #average_change = (monthly_change)/(count)   #((len(total_months)))

#         #for column in csvreader:
#             #last_value = int(column[1])   
                
#                 #average_change=(last_value - first_value)#(len(total_period)-1)
           






# #print(monthly_change/(len(total_months)-1))
# print("Financial Analysis")     
# print("----------------------------")       
# #print(f"Total Months: "+ str(len(total_months)))
# print(f"Total Months: "+ str(count))
# print(f"Total: $" + str(net_total))
# print(f"Average Change: $"+ str(average_change/(count-1)))
# print(f"Greatest Increase in Profits:" + str(greatest_increase))
# print(f"Greatest Decrease in Profits:" + str(greatest_decrease))
# print((382539-1088983)/85)
# #print(first_value)
# print(last_value)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     # Read each row of data after the header
#for row in csvreader:
        #print(row)
#DWIGHT EXAMPLE

budget_csv = os.path.join("/Users/kelcigriffin/python-challenge/PyBank/Resources/budget_data.csv")
print("budget_data.csv resource path is:    ",budget_csv)

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# read the header row first
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")
    csv_list = list(csv_reader)
    print(csv_list[0:5])


# for row in csv_list:
    # print(f"{row[0]}    {row[1]}")

# month list
month_list = [row[0] for row in csv_list]

#profit list
profit_list = [int(row[1]) for row in csv_list]

# total months
total_months = len(month_list)
#print(total_months)

# total profit
total_profit = sum(profit_list)
#print(total_profit)

# list of profit changes
profit_change = [profit_list[i] - profit_list[i-1] for i in range(1, total_months)]
print(profit_change[0:5])

month_change = [month_list[i] for i in range(1, total_months)]
print(month_change[0:5])

average_change = sum(profit_change)/(total_months-1)
print(average_change)

greatest_increase = max(profit_change)
#print(greatest_inc)
for i in range(total_months-1):
    #print(f"{i:3}  {profit_change[i]:12,}")
    if profit_change[i]==greatest_increase:
        greatest_increase_date = month_change[i]
        #print(f"{i:3}  {profit_change[i]:12,} {greatest_month:7}")
greatest_decrease = min(profit_change)
for i in range(total_months-1):
    #print(f"{i:3}  {profit_change[i]:12,}")
    if profit_change[i]==greatest_decrease:
        greatest_decrease_date = month_change[i]
        #print(f"{i:3}  {profit_change[i]:12,} {greatest_month:7}")


print("Financial Analysis")     
print("----------------------------")       
print(f"Total Months: "+ str(total_months))
print(f"Total: $" + str(total_profit))
print(f"Average Change: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_increase_date} (${greatest_decrease})")


#BAD PYPOLL
# candidate_column = str(row[2])
# candidate_change = [candidates[i] for i in range(2, total_votes)]
# candidate_change.append(candidate_column)
# print(candidate_change[0:5])









#         votes = {}

#         for row in csvreader:
#             candidate = str(row[2])
#             votes[candidate] = votes.get(candidate, 0) +1

# total = sum(votes.values())

# winner = max(votes, key=votes.get)
# loser = min(votes, key = votes.get)
        #ballot_column = []
        #county_column = []
        #candidate_column = []
#         #print(f"Header: {csv_header}")
        
#         #csv_list = list(csvreader)
#         #print(csv_list[0:5])
        
#         ballot_list = [row[0] for row in csvreader]
# #         #print(ballot_list)
#         total_votes = (len(ballot_list)+1)
#         candidate_column = str(row[2])
#         candidates = candidate_column 
        
#         for row in csvreader:
            
    
# total = sum(votes.values())

#         #row = next(csvreader)
#         #if candidates != candidates + row:
#                 #print(candidates)

#         #row = next(csvreader)


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
#dwight's formatting info 
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