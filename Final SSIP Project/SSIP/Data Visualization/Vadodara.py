import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the CSV file
csv_file_path = os.path.join(script_directory, 'Vadodara.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create a function to categorize the ratings
def categorize_rating(rating):
    if rating >= 8:
        return "Good Service"
    elif 4 < rating < 7:
        return "Average Service"
    else:
        return "Bad Service"

# Apply the categorization function to the 'Rating' column
df['Service Category'] = df['Rating'].apply(categorize_rating)

# Count the number of entries in each category
service_counts = df['Service Category'].value_counts()

# Define colors to match the second code snippet
colors = ['#ff6384', '#36a2eb', '#ffce56']

# Create a bar graph with matching colors and updated labels
plt.figure(figsize=(8, 6))
ax = service_counts.plot(kind='bar', color=colors)
ax.set_xticklabels(['Good', 'Average', 'Bad'], rotation=0)  # Update the labels
plt.xlabel('Service Categories')
plt.ylabel('Number of Ratings')
plt.title('Vadodara Police Station Working Reviews')
plt.show()
