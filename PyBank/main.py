# Import Dependencies
import os
import csv

# Create reference to CSV file
csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Initialize variables
    
    current_row = 0
    Total_Months = 0
    Total = 0 # Sum all values in Profit/Losses column
    Average_Change = 0.00
    Current_Change_in_Profit_Losses = 0.00
    Previous_Profit_Losses = 0    
    Total_Change_in_Profit_Losses = 0

    Greatest_Increase_in_Profits_month = ""
    Greatest_Increase_in_Profits_value = 0

    Greatest_Decrease_in_Profits_month = ""
    Greatest_Decrease_in_Profits_value = 0

    # Read through each row of data after the header
    for row in csv_reader:
        Total_Months += 1
        Total += int(row[1])
        if current_row == 0:
            #First row has no previous row
            Previous_Profit_Losses = int(row[1])

        Current_Change_in_Profit_Losses = int(row[1]) - Previous_Profit_Losses

        if Current_Change_in_Profit_Losses > 0 and Current_Change_in_Profit_Losses > Greatest_Increase_in_Profits_value:
            Greatest_Increase_in_Profits_month = row[0]
            Greatest_Increase_in_Profits_value = Current_Change_in_Profit_Losses
        
        if Current_Change_in_Profit_Losses < 0 and Current_Change_in_Profit_Losses < Greatest_Decrease_in_Profits_value:
            Greatest_Decrease_in_Profits_month = row[0]
            Greatest_Decrease_in_Profits_value = Current_Change_in_Profit_Losses
        

        Total_Change_in_Profit_Losses += Current_Change_in_Profit_Losses
        # print(f"Current_Change_in_Profit_Losses = {Current_Change_in_Profit_Losses}")
        Previous_Profit_Losses = int(row[1])

        current_row += 1


    Average_Change = Total_Change_in_Profit_Losses / (Total_Months - 1)

    # Printing to terminal
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${Average_Change:9.2f}")
    print(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits_month} (${Greatest_Increase_in_Profits_value:9.2f})")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits_month} (${Greatest_Decrease_in_Profits_value:9.2f})")

    #Exporting to a text file
    # Specify the file to write to
    output_path = os.path.join("Financial_Analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as text_file:

        text_file.write(f"Financial Analysis\n")
        text_file.write(f"----------------------------\n")
        text_file.write(f"Total Months: {Total_Months}\n")
        text_file.write(f"Total: ${Total}\n")
        text_file.write(f"Average Change: ${Average_Change:9.2f}\n")
        text_file.write(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits_month} (${Greatest_Increase_in_Profits_value:9.2f})\n")
        text_file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits_month} (${Greatest_Decrease_in_Profits_value:9.2f})\n")


