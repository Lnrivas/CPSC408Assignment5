#import MySQL
import mysql.connector

class db_operations():

    # constructor with connection path to database
    def __init__(self):
        #Make Connection
        self.connection = mysql.connector.connect(host = "localhost",
        user = "root",
        password = "cpsc-408",
        auth_plugin = 'mysql_native_password',
        database = "RideShare")
        #create cursor object
        self.cursor = self.connection.cursor()
        print("connection made")

    def create_user_table(self):
        query = '''
        CREATE TABLE User(
            UserID INT PRIMARY KEY NOT NULL,
            Name VARCHAR(50) NOT NULL,
            Email VARCHAR(100) NOT NULL UNIQUE,
            Password VARCHAR(100) NOT NULL,
            UserType ENUM('Rider', 'Driver') NOT NULL
        );
        '''
        self.cursor.execute(query)
        print("User table Created")

    def create_driver_table(self):
        query = '''
        CREATE TABLE Driver(
            DriverID INT PRIMARY KEY NOT NULL,
            Driver_mode BOOLEAN NOT NULL,
            Rating FLOAT NOT NULL
        );
        '''
        self.cursor.execute(query)
        print("Driver table Created")

    def create_trip_table(self):
        query = '''
        CREATE TABLE Trip(
            TripID INT PRIMARY KEY NOT NULL,
            RiderID INT NOT NULL,
            DriverID INT NOT NULL,
            Pickup_location VARCHAR(200) NOT NULL,
            Dropoff_location VARCHAR(200) NOT NULL,
            Pickup_time DATETIME NOT NULL,
            Dropoff_time DATETIME NOT NULL,
            Fare DECIMAL(7,2) NOT NULL
        );
        '''
        self.cursor.execute(query)
        print("Trip table Created")

    def create_rating_table(self):
        query = '''
        CREATE TABLE Rating(
            RatingID INT PRIMARY KEY NOT NULL,
            TripID INT NOT NULL,
            RiderID INT NOT NULL,
            DriverID INT NOT NULL,
            Rating_score INT NOT NULL CHECK(Rating_score BETWEEN 1 AND 5),
            Timestamp DATETIME NOT NULL
        );
        '''
        self.cursor.execute(query)
        print("Rating table Created")

    def add_record(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def select_record(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    # destructor that closes connection to database
    def destructor(self):
        self.connection.close()
