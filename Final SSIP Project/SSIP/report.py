import csv
import os

# Define the input CSV file
input_csv_file = 'Data.csv'

# Create a directory to store the separated files
output_dir = 'report_files'
os.makedirs(output_dir, exist_ok=True)

# Open the input CSV file
with open('Final SSIP Project/SSIP/Data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the CSV
    for row in csv_reader:
        district = row['District']
        
        # Create a new CSV file for each district
        output_csv_file = os.path.join(output_dir, f'{district}.csv')
        
        # Check if the CSV file for the district already exists, if not, create it
        if not os.path.exists(output_csv_file):
            with open(output_csv_file, 'w', newline='') as new_csv_file:
                fieldnames = csv_reader.fieldnames
                csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
        
        # Append the current row to the corresponding district CSV file
        with open(output_csv_file, 'a', newline='') as existing_csv_file:
            csv_writer = csv.DictWriter(existing_csv_file, fieldnames=fieldnames)
            csv_writer.writerow(row)

print("Separation of CSV files based on district is complete.")
