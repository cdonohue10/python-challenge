import csv
import os

print("Current Working Directory",os.getcwd())
cvspath = os.path.join("Resources", "budget_data.csv")

totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]

firstRow  = False

with open(cvspath) as revenueData:
   reader = csv.reader(revenueData)

   for row in reader:
        if firstRow:
            totalMonth = totalMonth + 1
            totalRevenue = totalRevenue + int(row[1])

            revenue_change = int(row[1]) - previousRevenue
            previousRevenue = int(row[1])
            month_of_change = month_of_change + [row[0]]
            
            revenue_change_list.append(revenue_change)

            if (revenue_change > greatestIncrease[1]):
                greatestIncrease[1] = revenue_change
                greatestIncrease[0] = row[0]

            if (revenue_change < greatestDecrease[1]):
                greatestDecrease[0] = row[0]
                greatestDecrease[1] = revenue_change
        else:
            firstRow = True

revenue_avg = sum(revenue_change_list) / len(revenue_change_list) 


output = (
    f"Total Months: {totalMonth}\n"
    f"Total: {totalRevenue}\n"
    f"Average Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
        )

print(output)
pathout = os.path.join("Resources", "budget_analysis.txt")
with open(pathout, "w") as txt_file:
    txt_file.write(output)
