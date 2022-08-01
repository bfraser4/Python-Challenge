import os
import csv


sum = 0 

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')


    header = next(csv_reader)
    for i in csv_reader: 
        # print(i)
        sum += int(i[1])
    # print(sum)

print(f'Total: ${sum}')
