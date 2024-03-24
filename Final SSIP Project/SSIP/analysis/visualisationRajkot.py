import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from your data (replace 'data.csv' with your actual file path)
data = pd.read_csv('report_files\Rajkot.csv')

# Create a function to categorize the ratings
def categorize_rating(rating):
    if rating >= 8:
        return "Good Service"
    elif rating > 4 and rating < 7:
        return "Average Service"
    else:
        return "Bad Service"

# Apply the categorization function to the 'Rating' column
data['Service Category'] = data['Rating'].apply(categorize_rating)

# Count the number of entries in each category
service_counts = data['Service Category'].value_counts()

# Create a pie chart to visualize the data
plt.figure(figsize=(8, 8))
plt.pie(service_counts, labels=service_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Rajkot Police Station Working Reviews')
plt.show()
