import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

# PyBank

dates = []
profitloss = []
total_months = 0
total_profit_loss = 0
average_change = 0

with open(pybank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        dates.append(row[0])
        profitloss.append(row[1])
# total months
for date in dates:
    total_months += date.count(date)
# total profit/loss
for numbers in profitloss:
    total_profit_loss += int(numbers)

change = []
for index in range(1, len(profitloss)):
    profitloss[index]
    calc = int(profitloss[index]) - int(profitloss[index - 1])

    change.append(calc)
    average_change = round(sum(change) / len(change), 2)
    maxcalc = max(change)
    mincalc = min(change)

# Print to Terminal
print("Financial Analysis")
print(f"\nTotal Months: {total_months}")
print(f"\nTotal: ${total_profit_loss}")
print(f"\nAverage Change: ${average_change}")
print(f"\nGreatest Increase in Profits: {date} (${maxcalc})")
print(f"\nGreatest Decrease in Profits: {date} (${mincalc})")

# Print to Text File
f = open("file.txt", "a")

f.write("Financial Analysis")
f.write(f"\nTotal Months: {total_months}")
f.write(f"\nTotal: ${total_profit_loss}")
f.write(f"\nAverage Change: ${average_change}")
f.write(f"\nGreatest Increase in Profits: {date} (${maxcalc})")
f.write(f"\nGreatest Decrease in Profits: {date} (${mincalc})")

f.close()
