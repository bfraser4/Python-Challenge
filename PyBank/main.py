import os 
import csv

#Set path 
csv_path = os.path.join('PyBank/Resources/budget_data.csv')

#Define variables
months = 0
profit_loss = 0
change = 0 
increase = 0
decrease = 0



with open(csv_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    for row in csv_reader:
        months = months + 1
        print(months)





#Print Analysis
print(f'Total Months: {months}')
print(f'Total: {profit_loss}')
print(f'Average Change: {change}')
print(f'Greatest Increase in Profits: {increase}')
print(f'Greatest Decrease in Profits: {decrease}')




