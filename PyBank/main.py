# importing csv
import os
csvpath = os.path.join('Resources', 'budget_data.csv')
import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    next(csvreader)
    first_month = next(csvreader)  
 # defining terms    
    print(first_month)
    months = 1
    amount = int(first_month[1])
    greatest_increase = 0
    greatest_decrease = 0
    previous_amount = int(first_month[1])
    total_difference = 0
    difference_count = 0
# creating loop of csv 
# looping through for total months and total amounts   
    for row in csvreader:
        months = months + 1
        amount = amount + int(row[1]) 
        difference = previous_amount - int(row[1])
# adding to loop to find average
        total_difference = total_difference + difference
        difference_count = difference_count + 1        
# looping to get increases and decreases        
        if difference < greatest_increase:
            greatest_increase = difference
        if difference > greatest_decrease:
            greatest_decrease = difference
        previous_amount = int(row[1])          
# calculating total months
    print(months)  
# calculating total amount of Profit/Losses
    print(amount)
# calculating average of changes in Profit/Losses
    print(total_difference/difference_count)
# Find the greatest increase in profits (date and amount)
    print(greatest_increase)
# Find the greatest decrease in losses
    print(greatest_decrease)          