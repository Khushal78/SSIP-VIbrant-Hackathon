import random
import csv

# Function to generate random data
def generate_random_data():
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Daniel", "Olivia", "Christopher", "Emma"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]
    districts = ["Surat", "Ahmedabad", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar", "Junagadh", "Anand", "Patan", "Mehsana"]
    comments = ["Excellent service", "Good service", "Average service", "Poor service", "Terrible service"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    police_station_address = f"R {random.randint(100, 999)} {random.choice(districts)} Police Station"
    district = random.choice(districts)
    comment = random.choice(comments)
    rating = random.randint(1, 10)
    
    return [first_name, last_name, email, police_station_address, district, comment, rating]

# Generate and save random data to CSV files
header = ["First Name", "Last Name", "Email", "Police Station Address", "District", "Comments", "Rating"]

with open("random_da5ta.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for _ in range(200):
        data = generate_random_data()
        writer.writerow(data)

print("Random data generated and saved to random_data.csv.")
