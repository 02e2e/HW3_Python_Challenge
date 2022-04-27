#import csv 

from multiprocessing import current_process
import os 
import csv


election_csv = os.path.join("Resources", "election_data.csv")
#file_output = os.path.join('analysis_folder', 'election_results.txt')
counter = 0 
candidate_list_results = {}
total_candidates=0
total_win_votes = 0 
total_win_candidate = ''

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    # Read through each row of data after the header
    for row in csv_reader:
        #counter for total votes cast 
        i = row[2]
        counter= counter + 1 
        
        if i in candidate_list_results:
            candidate_list_results[i]['votes']= candidate_list_results[i]['votes'] + 1
            
        else:
            #setting the candidate equal to the dictionary {}
            candidate_list_results[i]= {'votes': 1}
            
for i in candidate_list_results: 
    voter_percentage = (candidate_list_results[i]['votes']/counter) 

    format_percentage = '{:.03%}'.format(voter_percentage)
    candidate_list_results[i]['percentage']= format_percentage
    if candidate_list_results[i]['votes'] > total_win_votes:
        total_win_votes = candidate_list_results[i]['votes']
        # total_win_percentage = candidate_list_results[i]['percentage']
        winner = i

print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes: {counter}')
print(f'----------------------------')
for i in candidate_list_results: 
    print(f'{i}: {candidate_list_results[i]["percentage"]} ({candidate_list_results[i]["votes"]})' )   
print(f'----------------------------')
print(f'Winner: {winner}')
print(f'----------------------------')

#print out to text file 
output_file = os.path.join("election_final.txt")

with open(output_file, "w") as file:
    file.write(f'Election Results')
    file.write(f'----------------------------')
    file.write(f'Total Votes: {counter}')
    file.write(f'----------------------------')
    for i in candidate_list_results: 
        file.write(f'{i}: {candidate_list_results[i]["percentage"]} ({candidate_list_results[i]["votes"]})' )   
    file.write(f'----------------------------')
    file.write(f'Winner: {winner}')
    file.write(f'----------------------------')
