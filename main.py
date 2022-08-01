import os 
import csv

#Set path 
# csv_path = os.path.join('/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv')

#Define variables
months = 0
sum = 0
change = 0 
increase = 0
decrease = 0




with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    for row in csv_reader:
        months = months + 1
        sum += int(row[1])
     

    # for c in csv_reader:



        
    
 
      





#Print Analysis
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {months}')
print(f'Total: ${sum}')
print(f'Average Change: {change}')
# print(f'Greatest Increase in Profits: {increase}')
# print(f'Greatest Decrease in Profits: {decrease}')




