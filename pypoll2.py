import os
import csv

pypoll_csv = os.path.join("Resources", "election_data.csv")

with open(pypoll_csv, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Total number of votes 
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

# Create a new list from the CSV column to get candidates
candidates_list = list()
vote_tally = list()
for i in range(0, row_count):
  candidate = data[i][2]
  vote_tally.append(candidate)
  if candidate not in candidates_list:
    candidates_list.append(candidate)
    candidates_count = len(candidates_list)

# Votes for each candidate and percentage 
votes = list()
percentage = list()
for j in range(0, candidates_count):
  name = candidates_list[j]
  votes.append(vote_tally.count(name))
  vote_percentage = votes[j] / row_count
  percentage.append(vote_percentage)

# Election winner
winner = votes.index(max(votes))

# Results print to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {row_count:,}")
print("----------------------------")
for k in range (0,candidates_count):
    print(f"{candidates_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
print("----------------------------")
print(f"Winner: {candidates_list[winner]}")
print("----------------------------")

# Print to text file
f = open("pypoll.txt", "a")

f.write("Election Results")
f.write("----------------------------")
f.write(f"Total Votes: {row_count:,}")
f.write("----------------------------")

for p in range(0, candidates_count):
   f.write(f"{candidates_list[p]}: {percentage[p]:.3%} ({votes[p]:,})")

f.write("----------------------------")
f.write(f"Winner: {candidates_list[winner]}")
f.write("----------------------------")

f.close()
