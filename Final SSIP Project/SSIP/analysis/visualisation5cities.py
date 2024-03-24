import pandas as pd
import matplotlib.pyplot as plt

# Define the color mapping for service categories
colors = {
    'Good service': 'green',
    'Average service': 'orange',
    'Bad service': 'blue'
}

# Create a function to categorize the ratings
def categorize_rating(rating):
    if rating >= 8:
        return 'Good service'
    elif 4 < rating < 7:
        return 'Average service'
    else:
        return 'Bad service'

# Define the file paths for your 5 data CSV files
city_files = [
    "report_files\Ahmedabad.csv",
    "report_files\Gandhinagar.csv",
    "report_files\Rajkot.csv",
    "report_files\Surat.csv",
    "report_files\Vadodara.csv"
]

# Initialize an empty list to store the dataframes for each city
dfs = []

# Read the data from each CSV file and categorize the service
for city_file in city_files:
    df = pd.read_csv(city_file)
    df['Service Category'] = df['Rating'].apply(categorize_rating)
    dfs.append(df)

# Create a bar chart for each city
for i, df in enumerate(dfs):
    plt.figure()
    plt.bar(df['Service Category'].value_counts().index, df['Service Category'].value_counts(), color=[colors[c] for c in df['Service Category'].value_counts().index])
    plt.title(f"Reviews Across 5 Cities")
    plt.xlabel("Service Category")
    plt.ylabel("Count")
    plt.show()
