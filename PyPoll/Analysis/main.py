import os 
import csv

#Variables
votes = 0 
candidates = []
candidate_votes = dict()
candidate_list = [
    "Charles Casper Stockham",
    "Diana DeGette", 
    "Raymon Anthony Doane"
]
vote_percent = []

#Open CSV
with open ('election_data.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Remove header
    header = next(csv_reader)

    #Loop
    for row in csv_reader:
        votes = votes + 1 
        candidate = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1
    
# #Variables
voter_index = 1
voter_value = []


for candidate in candidates:
    total_votes = candidate_votes[candidate]
    vote_percent.append(round(float(total_votes) / float(votes) * 100,2))

# for key,value in candidate_votes.items():
    voter_value.append(round(int(total_votes),0))

#Find winner
winner = candidates[voter_index]

#Print Analysis 
print('Election Results')
print('------------------------')
print(f'Total Votes: {votes}')
print('------------------------')
print(f'{candidate_list[0]}: {vote_percent[0]}% ({voter_value[0]})')
print(f'{candidate_list[1]}: {vote_percent[1]}% ({voter_value[1]})')
print(f'{candidate_list[2]}: {vote_percent[2]}% ({voter_value[2]})')
print('------------------------')
print(f'Winner: {winner}')
print('------------------------')

#Output to txt.file
output = os.path.join("py_poll")
with open('py_poll.txt', 'w') as file: 
    file.write(f"Election Results\n")
    file.write(f"------------------------\n")
    file.write(f"Total Votes: {votes}\n")
    file.write(f"------------------------\n")
    file.write(f"{candidate_list[0]}: {vote_percent[0]}% ({voter_value[0]})\n")
    file.write(f"{candidate_list[1]}: {vote_percent[1]}% ({voter_value[1]})\n")
    file.write(f"{candidate_list[2]}: {vote_percent[2]}% ({voter_value[2]})\n")
    file.write(f"------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"------------------------\n")