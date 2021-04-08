#import modules
import os
import csv

#set directory path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

#locate directory
pypoll_path = os.path.join(dir_path, 'Resources')
os.chdir(pypoll_path)

votesTotal = 0
#create empty lists
candidateList = []
candidateUnique = []
candidateVoteTotal = []
candidateVotePercent = []

#read csv file
with open("PyPoll_data.csv","r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        #Skip header
        next(csvreader)
        
        #read each row of data after the header
        for row in csvreader:
            #find total number of votes
            votesTotal += 1
            #store candidates in empty list
            candidateList.append(row[2])

        for x in set(candidateList):
            #store unique candidates in empty list
            candidateUnique.append(x)
            #calculate total votes for each candidate
            votes = candidateList.count(x)
            #store votes in empty list
            candidateVoteTotal.append(votes)
            #calculate the percentage of votes each candidate recieved
            percent = (votes/votesTotal)*100
            #store percentages in empty list
            candidateVotePercent.append(percent)  
        
        #find the winner based on highest number of votes and define the candidate who won
        winnerVotes = max(candidateVoteTotal)
        winner = candidateUnique[candidateVoteTotal.index(winnerVotes)]

#print results to terminal
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

#define path for write file
pypoll_path_write = os.path.join(dir_path, 'analysis')
os.chdir(pypoll_path_write)

#write text file
with open("pypoll_analysis.txt", "w") as text:
    text.write("--------------------- \n")
    text.write("Election Results: \n")
    text.write("--------------------- \n")
    text.write(f"Total votes: {votesTotal} \n")
    text.write("--------------------- \n")
    for i in range(len(candidateUnique)):
        text.write(f"{candidateUnique[i]}: {round(candidateVotePercent[i], 2)}% ({candidateVoteTotal[i]}) \n")
    text.write("--------------------- \n")
    text.write(f"The winner is: {winner} \n")
    text.write("--------------------- \n")