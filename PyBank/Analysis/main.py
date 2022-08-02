import os 
import csv

#Define variables
months = 0
revenue = 0
total_change = []
total_profit_loss = 0
increase = 0
increase_month = ""
decrease = 0
decrease_month = ""
change = []


with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#Remove header
    header = next(csv_reader)
#Loop
    for row in csv_reader:
        months = months + 1
        revenue += int(row[1])
        # total_profit_loss = total_profit_loss + int(row[1])

        if months >1:
            total_change.append(revenue)
        # decrease = int(row[1])

        if int(row[1]) > increase:
            increase = int(row[1])
            increase_month = row[0]

        if int(row[1]) < decrease:
            decrease = int(row[1])
            decrease_month = row[0]

#Average change
# total_change = sum(change)
average_change = round(sum(total_change) / len(total_change), 2)


#Print Analysis
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {months}')
print(f'Total: ${revenue}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: ${increase}')
print(f'Greatest Decrease in Profits: ${decrease}')

#Output to txt.file

