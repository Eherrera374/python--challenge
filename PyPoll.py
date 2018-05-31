import os
import csv


file_num = 2


poll_csv = os.path.join("raw_data","election_data_" +str(file_num)+".csv")

poll = {}
TotalVotes = 0 

#print("Election Results")
#print("------------------------")


with open (poll_csv, newline = "") as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ",")


    next (csvreader, None)

    
    for row in csvreader: 
        
      TotalVotes += 1


      if row[2] in poll.keys():
            
        poll[row[2]] = poll[row[2]] + 1
      else:
        poll[row[2]] = 1    

#print ("Total Votes: " + str(TotalVotes))
#print("------------------------")

candidates = []
num_votes = []

for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)



vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/TotalVotes*100,1))   


cleanData = list(zip(candidates, num_votes, vote_percent))


winnerList= []  

for name in cleanData:
    if max(num_votes) == name[1]:
        winnerList.append(name[0])



winner = winnerList[0] 

outputFile = os.path.join('election_results_' +str(file_num)+ '.txt')

with open(outputFile, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(TotalVotes)+
    '\n------------------------- \n ' )
    for entry in cleanData:
        txtfile.writelines(entry[0] + ": "+ str(entry[2])+ "% (" + str(entry[1])+ ')\n')
    txtfile.writelines('------------------------- \nWinner:' + winner + '\n-------------------------')

with open(outputFile, 'r') as readfile:
    print(readfile.read())

     
 