import csv
import os

# Define the path to the CSV file
file_path = r"C:\Users\coleo\Python-Challenge\PyPoll\Resources\election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file and calculate election results
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        # Extract data from the row
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Create the "analysis" folder if it doesn't exist
analysis_folder = r"C:\Users\coleo\Python-Challenge\PyPoll\analysis"
os.makedirs(analysis_folder, exist_ok=True)

# Define the path for the analysis file
analysis_file_path = os.path.join(analysis_folder, "election_results.txt")

# Print election results and save to file
with open(analysis_file_path, 'w') as analysis_file:
    analysis_file.write("Election Results\n")
    analysis_file.write("-------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}\n")
    analysis_file.write("-------------------------\n")
    
    # Calculate and write results for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        analysis_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        
        # Check for the winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    analysis_file.write("-------------------------\n")
    analysis_file.write(f"Winner: {winner}\n")
    analysis_file.write("-------------------------\n")

print(f"Results have been saved to: {analysis_file_path}")
