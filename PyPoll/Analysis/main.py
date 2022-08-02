import os 
import csv

ballot_ID = 0 
candidates = []
candidate_votes = {}

with open ('election_data.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    for row in csv_reader:
        ballot_ID = ballot_ID + 1 

        # if row[2] not in candidates:
        #     candidates.append(row[2])
        #     candidate_votes[row[2]] = 1
        # else:
        #     candidate_votes[row[2]] += 1
    
    # winner = max(candidate_votes, key=candidate_votes.get)


    # for i in str(len(candidates)):
        # print(candidates)


#Print Analysis 
print('Election Results')
print('------------------------')
print(f'Total Votes: {ballot_ID}')
print('------------------------')
# for candidates in candidates:
#         votes = candidate_votes[candidates]
#         vote_percentage = float(votes) / float(ballot_ID) * 100
#         print(f'{candidates}: {vote_percentage:.3f}% ({votes})')
print('------------------------')
# print(f'Winner: {winner} ')
print('------------------------')

#Output to txt.file


