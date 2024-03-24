from flask import Flask, render_template, request, jsonify, redirect, url_for
import csv
import pymongo
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.npnpn7l.mongodb.net/?retryWrites=true&w=majority")
db = myclient["qr"]
feedback_collection = db["feedback"]

# Define the route to serve the feedback form
@app.route('/')
def feedback_form():
    return render_template('feedback.html')

# Define the route to handle form submission and store data in MongoDB and CSV
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        police_address = request.form['policeAddress']
        district = request.form['district']
        comments = request.form['comments']
        rating = request.form['rating']

        # Store data in MongoDB
        result = feedback_collection.insert_one({
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Police Station Address": police_address,
            "District": district,
            "Comments": comments,
            "Rating": rating
        })

        # Store data in CSV file
        with open('feedback.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, email, police_address, district, comments, rating])

        return redirect(url_for('feedback_form'))  # Redirect to the feedback form

# Define a route to list feedback data from MongoDB
@app.route('/feedback_list')
def feedback_list():
    feedback_data = feedback_collection.find({})
    return render_template('feedback_list.html', feedback_data=feedback_data)

# Define a route to run the Python code for generating graphs
@app.route('/run_python_code', methods=['POST'])
def run_python_code():
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
        plt.close()  # Close the plot to avoid displaying it in the browser

    return jsonify({'message': 'Python code executed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
