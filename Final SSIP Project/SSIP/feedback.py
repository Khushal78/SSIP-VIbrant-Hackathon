import random
import csv


indian_police_stations = [
    "Vadodara Police Station",
    "Surat Police Station",
    "Gandhinagar Police Station",
    "Ahemdabad Police Station",
    "Rajkot Police Station",
]
# Sample data for Indian first names and last names
indian_first_names = ["Aarav", "Neha", "Rahul", "Priya", "Sanjay", "Kavita"]
indian_last_names = ["Gupta", "Sharma", "Patel", "Singh", "Reddy", "Mukherjee"]
indian_districts = ["Vadodara", "Surat", "Gandhinagar", "Ahmedabad", "Rajkot"]
comments = ["Excellent service", "Good service", "Average service", "Poor service", "Terrible service"]

# Generate 200 random entries
entries = []
for _ in range(200):
    first_name = random.choice(indian_first_names)
    last_name = random.choice(indian_last_names)
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 100)}@example.com"
    police_station = random.choice(indian_police_stations)
    district = random.choice(indian_districts)
    comment = random.choice(comments)
    rating = random.randint(1, 10)  # Generate a random rating between 1 and 10
    entries.append([first_name, last_name, email, police_station, district, comment, rating])

# Write the entries to a CSV file
with open("indian_police_station_reviews.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["First Name", "Last Name", "Email", "Police Station Name", "District", "Comments", "Rating"])
    csv_writer.writerows(entries)
