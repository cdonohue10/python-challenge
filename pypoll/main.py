import os
import csv

csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:

   csvreader = csv.reader(csvfile, delimiter=",")

   print(csvreader)

   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")

   total_votes = 0
   candidates_list = []
   count_per_candidate = []
   percent_per_candidate = 0
   most_count_candidate = 0

   for row in csvreader:
       total_votes = csvreader.line_num - 1

       if total_votes > 1:
           new_candidates_list = candidates_list
           new_count_per_candidate = count_per_candidate

           if row[2] in new_candidates_list:
               candidate_index = int(new_candidates_list.index(row[2]))
               new_count_per_candidate[candidate_index] += 1
               percent_per_candidate = [round((count/(total_votes-1))*100,2) for count in new_count_per_candidate]
               winner = max(new_count_per_candidate)
               winner_name = new_candidates_list[int(new_count_per_candidate.index(winner))]
           else:
               candidates_list.append(row[2])
               count_per_candidate.append(1)


print("-------------------------------")
print("Election Results")
print("-------------------------------")

print ("Total Votes: " + str(total_votes))
print("-------------------------------")

for i in range(4):
   print(new_candidates_list[i] + ": " + str(percent_per_candidate[i]) + "%   " + str(new_count_per_candidate[i]))

print("-------------------------------")
print("Winner: " + winner_name)
print("-------------------------------")



#--------------------------- output to text file

print("-------------------------------", file=open("Poll.analysis.txt", "a"))
print("Election Results", file=open("Poll.analysis.txt", "a"))
print("-------------------------------", file=open("Poll.analysis.txt", "a"))

print ("Total Votes: " + str(total_votes), file=open("Poll.analysis.txt", "a"))
print("-------------------------------", file=open("Poll.analysis.txt", "a"))

for i in range(4):
   print(new_candidates_list[i] + ": " + str(percent_per_candidate[i]) + "%   " + str(new_count_per_candidate[i]), file=open("Poll.analysis.txt", "a"))

print("-------------------------------", file=open("Poll.analysis.txt", "a"))
print("Winner: " + winner_name, file=open("Poll.analysis.txt", "a"))
print("-------------------------------", file=open("Poll.analysis.txt", "a"))


