import pandas as pd
import matplotlib.pyplot as plt

# List of data files
data_files = [
    "report_files\Ahmedabad.csv",
    "report_files\Gandhinagar.csv",
    "report_files\Rajkot.csv",
    "report_files\Vadodara.csv",
    "report_files\Surat.csv"
]

# Initialize counters for different service categories
good_service = 0
average_service = 0
bad_service = 0

# Loop through each data file
for file in data_files:
    data = pd.read_csv(file)
    
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

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(service_labels, service_counts, color=['green', 'orange', 'blue'])
plt.xlabel('Service Categories')
plt.ylabel('Number of Ratings')
plt.title('Distribution of Ratings Across 5 Cities')
plt.show()
