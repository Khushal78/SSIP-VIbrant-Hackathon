import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the directory where the files are located relative to the script
directory = os.path.join(script_directory)

# List of data files
data_files = [
    "Ahmedabad.csv",
    "Gandhinagar.csv",
    "Rajkot.csv",
    "Vadodara.csv",
    "Surat.csv"
]

# Initialize counters for different service categories
good_service = 0
average_service = 0
bad_service = 0

# Loop through each data file
for file in data_files:
    file_path = os.path.join(directory, file)
    data = pd.read_csv(file_path)
    
    # Categorize ratings into service categories
    for rating in data['Rating']:
        if rating >= 8:
            good_service += 1
        elif 4 < rating < 7:
            average_service += 1
        else:
            bad_service += 1

# Data for the bar graph
service_labels = ['Good Service', 'Average Service', 'Bad Service']
service_counts = [good_service, average_service, bad_service]

# Define colors to match visualisation.html
colors = ['#ff6384', '#36a2eb', '#ffce56']

# Create a bar graph with matching colors
plt.figure(figsize=(10, 6))
plt.bar(service_labels, service_counts, color=colors)
plt.xlabel('Service Categories')
plt.ylabel('Number of Ratings')
plt.title('Distribution of Ratings Across 5 Cities')
plt.show()
