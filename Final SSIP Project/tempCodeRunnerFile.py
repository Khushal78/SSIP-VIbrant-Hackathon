from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Define the route to serve the feedback form
@app.route('/')
def feedback_form():
    return render_template('feedback.html')

# Define the route to handle form submission and store data in a CSV file
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

        # Write data to a CSV file
        with open('feedback.csv', mode='a', newline='') as csv_file:
            fieldnames = ['First Name', 'Last Name', 'Email', 'Police Station Address', 'District', 'Comments', 'Rating']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:  # Check if the file is empty
                writer.writeheader()  # Write header only if the file is empty
            writer.writerow({
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'Police Station Address': police_address,
                'District': district,
                'Comments': comments,
                'Rating': rating
            })

        return redirect(url_for('feedback_form'))  # Redirect to the feedback form

if __name__ == '__main__':
    app.run(debug=True)
