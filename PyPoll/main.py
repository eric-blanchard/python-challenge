import os
import csv

# identify the data source:
election_csv = os.path.join("PyPoll/Resources", "election_data.csv")

# specify the analysis output file:
output_file = os.path.join("PyPoll/analysis", "Election Results.txt")

# declare lists:
votes = []
candidates = []

#declare variables:
winningCount = 0
winner = ""

with open(election_csv, encoding="utf-8") as csv_file:
    election = csv.reader(csv_file, delimiter=",")
    next(election) # skip the first row because it's just the headers

    print("Election Results")

    with open(output_file, "w",  encoding="utf-8") as output: # create output file and begin data:
        output.write("Election Results")
        output.write("\n")
        output.write("\n")
        output.write("----------------------------")
        output.write("\n")
        output.write("\n")

    for row in election:
        votes.append(row[2]) # append the name voted for on the current row to "votes"

    print(f"Total Votes: {len(votes)}") # print total votes to terminal

    with open(output_file, "a", encoding="utf-8") as output: # append to output file total votes:
        output.write(f"Total Votes: {len(votes)}")
        output.write("\n")
        output.write("\n")
        output.write("----------------------------")
        output.write("\n")
        output.write("\n")

    candidates = list(set(votes)) # assign to "candidates" each unique name that was voted for

    for name in candidates:
        voteCount = votes.count(name)
        print(f"{name}: {round(voteCount/len(votes)*100,3)}% ({voteCount})") # print candidate's result to terminal

        if voteCount > winningCount: # check if current candidate is winning, update "winningCount" and "winner" as appropriate:
            winningCount = voteCount
            winner = name

        with open(output_file, "a", encoding="utf-8") as output: # append to output file candidate name and votes for each:
            output.write(f"{name}: {round(voteCount/len(votes)*100,3)}% ({voteCount})")
            output.write("\n")
            output.write("\n")

    print(f"Winner: {winner}") # print winner to terminal

    with open(output_file, "a", encoding="utf-8") as output: # append to output file the winner:
        output.write("----------------------------")
        output.write("\n")
        output.write("\n")
        output.write(f"Winner: {winner}")
        output.write("\n")
        output.write("\n")
        output.write("----------------------------")