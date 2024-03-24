import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the paths to your CSV files
data_paths = [
    'report_files\Ahmedabad.csv',
    'report_files\Gandhinagar.csv',
    'report_files\Rajkot.csv',
    'report_files\Surat.csv',
    'report_files\Vadodara.csv'
]

# Define rating categories
def categorize_rating(rating):
    if rating >= 8:
        return 'Good Service'
    elif 4 < rating < 7:
        return 'Average Service'
    else:
        return 'Bad Service'

# Initialize empty dictionaries to store the categorized data
categorized_data = {'Good Service': [], 'Average Service': [], 'Bad Service': []}

# Load and process data from each CSV
for data_path in data_paths:
    # Load the data
    data = pd.read_csv(data_path)
    
    # Categorize the ratings
    data['Service Category'] = data['Rating'].apply(categorize_rating)
    
    # Count the occurrences of each service category
    category_counts = data['Service Category'].value_counts()
    
    # Add the counts to the categorized data dictionary
    for category, count in category_counts.items():
        categorized_data[category].append(count)

# Create a bar chart for each city
cities = ['Ahmedabad', 'Gandhinagar', 'Rajkot', 'Surat', 'Vadodara']
categories = ['Good Service', 'Average Service', 'Bad Service']
width = 0.3

for category in categories:
    category_counts = categorized_data[category]
    x = range(len(cities))
    plt.bar([i for i in x], category_counts, width=width, label=category)

plt.xlabel('City')
plt.ylabel('Number of Reviews')
plt.title('Service Rating Distribution by City')
plt.xticks([i for i in x], cities)
plt.legend()
plt.tight_layout()

# Show the chart
plt.show()
