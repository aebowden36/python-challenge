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


with open("PyPoll_data.csv","r") as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter = ',')

        print(csvreader)
    #Skip header
        next(csvreader)
        votesTotal = 0

        #read each row of data after the header
        for row in csvreader:
            #print(row[0])
            votesTotal += 1
print(f"Total votes: {votesTotal}")