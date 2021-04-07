#import modules
import os
import csv

#set directory path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

#locate directory
pypoll_path = os.path.join(dir_path, 'Resources')
print(pypoll_path)
print(type(pypoll_path))
os.chdir(pypoll_path)

votesTotal = 0
#create empty lists
candidateList = []
candidateUnique = []
candidateVoteTotal = []
candidateVotePercent = []
with open("PyPoll_data.csv","r") as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter = ',')
    #Skip header
        next(csvreader)
        
        
        #read each row of data after the header
        for row in csvreader:
            #find total number of votes
            votesTotal += 1

            candidateList.append(row[2])

        for x in set(candidateList):
            candidateUnique.append(x)
            y = candidateList.count(x)
            candidateVoteTotal.append(y)
            z = (y/votesTotal)*100
            candidateVotePercent.append(z)  
        winnerVotes = max(candidateVoteTotal)
        winner = candidateUnique[candidateVoteTotal.index(winnerVotes)]

print("---------------------")
print("Election Results:")
print("---------------------")
print(f"Total votes: {votesTotal}")
print("---------------------")
for i in range(len(candidateUnique)):
    print(f"{candidateUnique[i]}: {round(candidateVotePercent[i], 2)}% ({candidateVoteTotal[i]})")
print("---------------------")
print(f"The winner is: {winner}")
print("---------------------")

# pypoll_path_write = os.path.join(dir_path, 'analysis')
# print(pypoll_path_write)
# print(type(pypoll_path_write))
# os.chdir(pypoll_path_write)

# with open("pypoll_analysis.txt", "w") as text:
#     text.write("--------------------- \n")
#     text.write("Election Results: \n")
#     text.write("--------------------- \n")
#     text.write(f"Total votes: {votesTotal} \n")
#     text.write("--------------------- \n")
#     for i in range(len(candidateUnique)):
#         text.write(f"{candidateUnique[i]}: {round(candidateVotePercent[i], 2)}% ({candidateVoteTotal[i]}) \n")
#     text.write("--------------------- \n")
#     text.write(f"The winner is: {winner} \n")
#     text.write("--------------------- \n")