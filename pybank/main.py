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

#lists to store data in
profit = []
monthlyChange = []
date = []

monthTotal = 0
netTotal = 0
totalChange = 0
initialProfit = 0

with open("PyBank_budget_data.csv","r") as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter = ',')

        print(csvreader)
    #Skip header
        next(csvreader)
        

        #read each row of data after the header
        for row in csvreader:
            
            #find the total number of months in the data
            monthTotal += 1
            date.append(row[0])
            #find the total profit
            profit.append(row[1])
            netTotal += float(row[1])

            finalProfit = int(row[1])
            monthlyChangeProfit = finalProfit - initialProfit
            monthlyChange.append(monthlyChangeProfit)
            
            totalChange += monthlyChangeProfit
            initialProfit = finalProfit

            averageChange = (totalChange/monthTotal)

            increase = max(monthlyChange)
            decrease = min(monthlyChange)

            increaseDate = date[monthlyChange.index(increase)]
            decreaseDate = date[monthlyChange.index(decrease)]

print("---------------------")
print("Financial Analysis:")
print("---------------------")
print(f"Total months: {monthTotal}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase: {increaseDate} ${increase}")
print(f"Greatest Decrease: {decreaseDate} ${decrease}")
print("---------------------")