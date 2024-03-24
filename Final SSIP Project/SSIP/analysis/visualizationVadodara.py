import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
data = pd.read_csv('report_files\Vadodara.csv')

# Create a function to categorize the ratings
def categorize_rating(rating):
    if rating >= 8:
        return "Good Service"
    elif 4 < rating < 7:
        return "Average Service"
    else:
        return "Bad Service"

# Apply the categorization function to the 'Rating' column
data['Service Category'] = data['Rating'].apply(categorize_rating)

# Count the number of entries in each category
service_counts = data['Service Category'].value_counts()

# Create a pie chart to visualize the data
plt.figure(figsize=(8, 6))
plt.pie(service_counts, labels=service_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Vadodara Police Station Working Reviews')
plt.show()
