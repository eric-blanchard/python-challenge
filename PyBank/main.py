import os
import csv

# identify the data source:
budget_csv = os.path.join("PyBank/Resources", "budget_data.csv")

# specify the analysis output file:
output_file = os.path.join("PyBank/analysis", "Budget Analysis.txt")

# declare lists:
months = []
gains = []
changes = []

# declare misc varibles:
greatestIncrease = 0
greatestDecrease = 0
gainTracker = 0
increaseMonth = ""
decreaseMonth = ""

with open(budget_csv, encoding="utf-8") as csv_file:
    budget = csv.reader(csv_file, delimiter=",")
    next(budget) # skip the first row because it's just the headers

    for row in budget:
        months.append(row[0]) # append month data to the list "months"
        gains.append(int(row[1])) # convert profit or loss to integers then append to the list "gains"

        if len(months) > 1: # only do this step after the first time through the for loop
            changes.append(int(row[1]) - gainTracker) # append the change in profit compared to the previous row's profit or loss

            if (int(row[1]) - gainTracker) > greatestIncrease: # if current increase is greater than the greatest increase so far
                greatestIncrease = int(row[1]) - gainTracker # update "greatestIncrease" to the current increase
                increaseMonth = row[0] # set "increaseMonth" to the current increase's associated month

            if (int(row[1]) - gainTracker) < greatestDecrease: # if current decrease is greater than the greatest decrease so far
                greatestDecrease = int(row[1]) - gainTracker # update "greatestDecrease" to the current decrease
                decreaseMonth = row[0] # set "decreaseMonth" to the current decrease's associated month

        gainTracker = int(row[1]) # sets "gainTracker" to the current row's profit or loss

# print analysis to the terminal:
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(gains)}")
print(f"Average Change: ${(round(sum(changes)/len(changes),2))}")
print(f"Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {decreaseMonth} (${greatestDecrease})")

# write all the results to the output file:
with open(output_file, "w",  encoding="utf-8") as output:
    output.write("Financial Analysis")
    output.write("\n")
    output.write("\n")
    output.write("----------------------------")
    output.write("\n")
    output.write("\n")
    output.write(f"Total Months: {len(months)}")
    output.write("\n")
    output.write("\n")
    output.write(f"Total: ${sum(gains)}")
    output.write("\n")
    output.write("\n")
    output.write(f"Average Change: ${(round(sum(changes)/len(changes),2))}")
    output.write("\n")
    output.write("\n")
    output.write(f"Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})")
    output.write("\n")
    output.write("\n")
    output.write(f"Greatest Decrease in Profits: {decreaseMonth} (${greatestDecrease})")
