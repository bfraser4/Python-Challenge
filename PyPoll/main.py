import os 
import csv

ballot_ID = 0 

with open ('election_data.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    for row in csv_reader:
        ballot_ID = ballot_ID + 1 
        


#Print Analysis 
print('Election Results')
print('------------------------')
print(f'Total Votes: {ballot_ID}')
print('------------------------')


print('------------------------')
print('Winner: {}')
print('------------------------')



