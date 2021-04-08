#import modules
import os
import csv

#set directory path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

#locate directory
pybank_path = os.path.join(dir_path, 'Resources')
os.chdir(pybank_path)

#lists to store data in
profit = []
monthlyChange = []
month = []

monthTotal = 0
netTotal = 0
totalChange = 0
initialProfit = 0

#read csv file
with open("PyBank_budget_data.csv","r") as csvfile: 
        csvreader = csv.reader(csvfile, delimiter = ',')

        #Skip header
        next(csvreader)
        

        #read each row of data after the header
        for row in csvreader:
            
            #find the total number of months in the data
            #store the month in empty list
            monthTotal += 1
            month.append(row[0])
            
            #store the profit information in empty list
            #find the total profit
            profit.append(row[1])
            netTotal += int(row[1])

            #calculate the monthly profit changes
            finalProfit = int(row[1])
            monthlyChangeProfit = finalProfit - initialProfit
            
            #store monthly changes in empty list
            monthlyChange.append(monthlyChangeProfit)
            
            totalChange += monthlyChangeProfit
            initialProfit = finalProfit
            
            #calculate the average profit change
            averageChange = (totalChange/monthTotal)
            #find the greatest increase and decrease
            increase = max(monthlyChange)
            decrease = min(monthlyChange)
            #find the months/years of the greatest increase and greatest decrease
            increaseDate = month[monthlyChange.index(increase)]
            decreaseDate = month[monthlyChange.index(decrease)]
#print results to the terminal
print("---------------------")
print("Financial Analysis:")
print("---------------------")
print(f"Total months: {monthTotal}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${round(averageChange, 2)}")
print(f"Greatest Increase in Profits: {increaseDate} ${increase}")
print(f"Greatest Decrease in Profits: {decreaseDate} ${decrease}")
print("---------------------")

#define path for write file
pybank_path_write = os.path.join(dir_path, 'analysis')
os.chdir(pybank_path_write)

#write text file
with open("pybank_analysis.txt", "w") as text:
    text.write("--------------------- \n")
    text.write("Financial Analysis: \n")
    text.write("--------------------- \n")
    text.write(f"Total months: {monthTotal} \n")
    text.write(f"Total: ${netTotal} \n")
    text.write(f"Average Change: ${round(averageChange, 2)} \n")
    text.write(f"Greatest Increase in Profits: {increaseDate} ${increase} \n")
    text.write(f"Greatest Decrease in Profits: {decreaseDate} ${decrease} \n")
    text.write("--------------------- \n")