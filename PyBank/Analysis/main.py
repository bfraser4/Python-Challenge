import os 
import csv

#Define variables
months = 0
revenue = 0
total_profit_loss = 0
date = []
change = []
change_row = []

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#Remove header
    header = next(csv_reader)
#Loop
    for row in csv_reader:
        months = months + 1
        revenue += int(row[1])
        total_profit_loss = total_profit_loss + int(row[1])
        date.append(row[0])
        change.append(int(row[1]))

    for i in range(1, len(change)):
        change_row.append(change[i] - change[i - 1])
        average_change = round(sum(change_row) / len(change_row),2)

        increase = max(change_row)
        decrease = min(change_row)

        increase_month = str(date[change_row.index(increase)])
        decrease_month = str(date[change_row.index(decrease)])


#Print Analysis
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {months}')
print(f'Total: ${revenue}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_month} (${increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${decrease})')

#Output to txt.file
output = os.path.join("py_bank.txt")
with open('py_bank.txt', 'w') as file: 
    file.write(f"Financial Analysis\n")
    file.write(f"------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${revenue}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {increase_month} (${increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_month} (${decrease})\n")


