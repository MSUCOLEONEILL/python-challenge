import csv

# Define the path to the CSV file
file_path = r"C:\Users\coleo\Python-Challenge\PyBank\Resources\Budget_Data.csv"





# Initialize variables to store financial analysis results
total_months = 0
net_total = 0
changes = []
dates = []

# Read the CSV file and calculate financial analysis metrics
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Initialize variables for tracking changes
    prev_profit_loss = 0

    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the change in profit/loss
        change = profit_loss - prev_profit_loss

        # Update previous profit/loss for the next iteration
        prev_profit_loss = profit_loss

        # Update total months and net total
        total_months += 1
        net_total += profit_loss

        # Store changes and corresponding dates
        if total_months > 1:
            changes.append(change)
            dates.append(date)

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Get the corresponding dates for the greatest increase and decrease
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]

# Define the path for the analysis file
analysis_file_path = "C:\\Users\\coleo\\Python-Challenge\\PyBank\\Analysis\\financial_analysis.txt"

# Write the financial analysis results to a text file
with open(analysis_file_path, 'w') as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("-------------------------\n")
    analysis_file.write(f"Total Months: {total_months}\n")
    analysis_file.write(f"Total: ${net_total}\n")
    analysis_file.write(f"Average Change: ${round(average_change, 2)}\n")
    analysis_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

# Print a message indicating that the analysis has been saved
print(f"Financial analysis has been saved to: {analysis_file_path}")

