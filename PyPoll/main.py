# Import Dependencies
import os
import csv

# Create reference to CSV file
csv_path = os.path.join("Resources", "election_data.csv")



# Open and read csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Initialize variables
    Total_Votes = 0
    new = 0
    

    #candidate = {"candidate_name":[],"candidate_total_votes":[],"candidate_percent":[]};
    candidate = dict()

    # Read through each row of data after the header
    for row in csv_reader:
        Total_Votes += 1
        # ---------------------------------------------------------------
        if row[2] in candidate:
            new = candidate[row[2]] + 1
            candidate.update({row[2]: new})
        else:
            candidate.update({row[2]: 1})

    candidate_sorted = sorted(candidate.items(), key=lambda x: x[1], reverse=True)

    #print("Dictionary after updation:",candidate)               
    #print("Dictionary after sorted:",candidate_sorted)           


    # Printing to terminal
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {Total_Votes}")
    print(f"----------------------------")
    for each_candidate in candidate_sorted:
        percent_of_votes = each_candidate[1] / Total_Votes * 100
        print(f"{each_candidate[0]:10}: {percent_of_votes:2.3f}%   ({each_candidate[1]})")
    print(f"----------------------------")
    print(f"Winner: {candidate_sorted[0][0]}")
    print(f"----------------------------")
    
    #Exporting to a text file
    # Specify the file to write to
    output_path = os.path.join("Election_Results.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as text_file:

        text_file.write(f"Election Results\n")
        text_file.write(f"----------------------------\n")
        text_file.write(f"Total Votes: {Total_Votes}\n")
        text_file.write(f"----------------------------\n")
        for each_candidate in candidate_sorted:
            percent_of_votes = each_candidate[1] / Total_Votes * 100
            text_file.write(f"{each_candidate[0]:10}: {percent_of_votes:2.3f}%   ({each_candidate[1]})\n")
        text_file.write(f"----------------------------\n")
        text_file.write(f"Winner: {candidate_sorted[0][0]}\n")
        text_file.write(f"----------------------------\n")

