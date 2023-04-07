import pandas as pd
from db_operations import db_operations

def populate_database():
    db = db_operations("RideShare")
    db.create_tables()

    # Read CSV files
    users = pd.read_csv('data/users.csv')
    drivers = pd.read_csv('data/drivers.csv')
    trips = pd.read_csv('data/trips.csv')
    ratings = pd.read_csv('data/ratings.csv')

    # Insert records from CSV files to the database

    # Users
    for _, row in users.iterrows():
        db.insert_user(row['UserID'], row['Name'], row['UserType'])

    # Drivers
    for _, row in drivers.iterrows():
        db.insert_driver(row['DriverID'], row['Driver_mode'], row['Rating'])

    # Trips
    for _, row in trips.iterrows():
        db.insert_trip(row['RiderID'], row['DriverID'], row['Pickup_location'], row['Dropoff_location'], row['Fare'])

    # Ratings
    for _, row in ratings.iterrows():
        db.insert_rating(row['TripID'], row['RiderID'], row['DriverID'], row['Rating_score'])

    print("Database populated successfully.")
    db.close()

if __name__ == "__main__":
    populate_database()
