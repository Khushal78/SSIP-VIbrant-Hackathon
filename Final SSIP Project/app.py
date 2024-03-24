from flask import Flask, render_template, request, jsonify, redirect, url_for
import csv
import pymongo

app = Flask(__name__)
# Home page
@app.route('/')
def homepage():
    return render_template('login.html')

# Registration form
@app.route('/sign_up')
def registration_form():
    return render_template('D:\Downloads\Final SSIP Project\templates\register.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('n')
    email = request.form.get('el')
    password = request.form.get('cpsw')
    
    # Save data to a CSV file (you can replace 'registration.csv' with your desired filename)
    with open('registration.csv', mode='a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])
    
    return redirect(url_for('login_form'))
@app.route('/login')
def login_form():
    return render_template('login.html')

# Check login credentials
@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form.get('n')
    password = request.form.get('psw')
    
    # Check the CSV file for the given username and password
    with open('registration.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[2] == password:  # Check username and password
                return redirect(url_for('main_page'))  # Redirect to job listings after successful login
    
    return redirect(url_for('login_form'))

if __name__ == '__main__':
    app.run(debug=True)