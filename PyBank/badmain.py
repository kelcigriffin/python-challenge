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
month_num = len(month_list)
print(month_num)

# total profit
profit_tot = sum(profit_list)
print(profit_tot)

# list of profit changes
profit_change = [profit_list[i] - profit_list[i-1] for i in range(1, month_num)]
print(profit_change[0:5])

month_change = [month_list[i] for i in range(1, month_num)]
print(month_change[0:5])

average_change = sum(profit_change)/(month_num-1)
print(average_change)

greatest_inc = max(profit_change)
#print(greatest_inc)
for i in range(month_num-1):
    #print(f"{i:3}  {profit_change[i]:12,}")
    if profit_change[i]==greatest_inc:
        greatest_month = month_change[i]
        #print(f"{i:3}  {profit_change[i]:12,} {greatest_month:7}")
greatest_dec = min(profit_change)
for i in range(month_num-1):
    #print(f"{i:3}  {profit_change[i]:12,}")
    if profit_change[i]==greatest_dec:
        least_month = month_change[i]
        #print(f"{i:3}  {profit_change[i]:12,} {greatest_month:7}")
print(greatest_dec)
print(greatest_month, greatest_inc)
print(least_month, greatest_dec)