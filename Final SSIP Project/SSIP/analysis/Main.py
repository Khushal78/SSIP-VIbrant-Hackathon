import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Final SSIP Project/SSIP/data2.csv')

# Create a function to categorize the ratings
def categorize_rating(rating):
    if rating >= 8:
        return "Good Service"
    elif 4 <= rating < 7:
        return "Average Service"
    else:
        return "Bad Service"

# Apply the categorization function to the 'Rating' column
df['Service Category'] = df['Rating'].apply(categorize_rating)

# Count the number of entries in each category for each district
service_counts_district_wise = df.groupby(['District', 'Service Category']).size().unstack(fill_value=0)

# Define custom colors
colors = ['#66b3ff','#99ff99','#ffcc99']

# Create a bar graph for each district
for district in df['District'].unique():
    district_data = service_counts_district_wise.loc[district]
    
    plt.figure(figsize=(10, 6))
    district_data.plot(kind='bar', color=colors, edgecolor='black')
    plt.title(f'Service Category Distribution in {district}')
    plt.xlabel('Service Category')
    plt.ylabel('Number of Entries')
    plt.savefig(f'Final SSIP Project/SSIP/{district}_service_distribution.png')  # Save the figure with the correct path
    plt.show()


