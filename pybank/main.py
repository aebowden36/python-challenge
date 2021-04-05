#import modules
import os
import csv

#set directory path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

#locate directory
pybank_path = os.path.join(dir_path, 'Resources')
print(pybank_path)
print(type(pybank_path))
os.chdir(pybank_path)


with open("PyBank_budget_data.csv","r") as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter = ',')

        print(csvreader)
    #Skip header
        next(csvreader)
        monthTotal=0
        netTotal=0

        #read each row of data after the header
        for row in csvreader:
            #print(row[0])
            monthTotal += 1
            netTotal += float(row[1])
            #averageChange
            #increase
            #decrease
            
print("Financial Analysis:")
print("---------------------")
print(f"Total months: {monthTotal}")
print(f"Total: ${netTotal}")
