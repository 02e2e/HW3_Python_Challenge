#import csv 

from multiprocessing import current_process
import os 
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_profit_losses = 0 
months = 0 
current = 0 
last = 0 
total_change = 0
#list to track greatest increase in profits 
#list to track greatest decrease in profits 
tracking = []
date_track = []
last = 0 
row_count = 0
net_change = 0 
greatest_change =0
greatest_month= ''
least_change = 999999999 
least_month = ''
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    # Read through each row of data after the header
    for row in csv_reader:
        #checked and printed the data after the header 
        #print(row)
        #column index row[1] is profit/losses
        total_profit_losses = total_profit_losses + int(row[1])
        #print (total_profit_losses)
        months = str(row[0])
        #print(months)
        current = int(row[1]) 
        tracking.append(current)
        date_track.append(months)
        #no net change on first
        if row_count > 0:
            net_change = tracking[row_count] - tracking[row_count - 1] 
            total_change = total_change + net_change 
        row_count = row_count + 1
        if net_change > greatest_change: 
            greatest_change = net_change 
            greatest_month = row[0]
        if net_change < least_change: 
            least_change = net_change 
            least_month = row[0]

#need help formatting the numbers so that it prints as per the instructions ??
#print out to a text file ??

print(f'Financial Analysis')    
print(f' --------------------------')  
average_change = total_change / (row_count - 1)                   
print(f'The total number of months: ', row_count)       
print(f'The total change over the period: ', total_profit_losses) 
print(f'The average change over the entire period: ', average_change)
print(f'The greatest increase over the entire period and month: ', greatest_change, greatest_month) 
print(f'The greatest decrease in profits over the entire period and month: ' , least_change, least_month) 
      
output_file = os.path.join("pybank.txt")

with open(output_file, "w") as file:
    file.write(f'Financial Analysis')    
    file.write(f' --------------------------')  
    average_change = total_change / (row_count - 1)                   
    file.write(f'The total number of months:  {row_count}')  
    file.write(f'The total change over the period: {total_profit_losses}') 
    file.write(f'The average change over the entire period: {average_change}')
    file.write(f'The greatest increase over the entire period and month:{greatest_change}, {greatest_month}') 
    file.write(f'The greatest decrease in profits over the entire period and month: {least_change} {least_month}') 

