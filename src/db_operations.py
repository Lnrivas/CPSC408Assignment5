import mysql.connector

class db_operations():

    # constructor with connection path to database
    def __init__(self, db_name, user, password):

        self.db_name = db_name

        # Make Connection
        self.connection = mysql.connector.connect(host = "localhost",
            user = user,
            password = password,
            auth_plugin = 'mysql_native_password')

        # Create cursor object
        self.cursor = self.connection.cursor()

        # Check if database exists
        self.cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in self.cursor.fetchall()]
        if db_name not in databases:
            self.create_database(self.db_name, user, password)
            self.import_db('rideshare_dump.sql')
            
        self.cursor.execute(f"USE {db_name}")

        print("Connection Made.")

    def import_db(self, dump_file, user, password):
        try:
            connection_import = mysql.connector.connect(host="localhost",
                                                    user=user,
                                                    password=password,
                                                    auth_plugin='mysql_native_password',
                                                    database=self.db_name)
            cursor_import = connection_import.cursor()

            with open(dump_file, 'r') as file:
                file_content = file.read()
                queries = file_content.split(';')
                for query in queries:
                    if query.strip():
                        cursor_import.execute(query)
                connection_import.commit()

        except Exception as e:
            print(f"Error importing database: {e}")
        finally:
            cursor_import.close()
            connection_import.close()


    # Attempts to create the database if not found
    def create_database(self, db_name):
        try:
            self.cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
            result = self.cursor.fetchone()
            
            if result:
                print(f"Database '{db_name}' already exists.")
            else:
                self.cursor.execute(f"CREATE DATABASE {db_name}")
                print(f"Database '{db_name}' created successfully.")
            
        except mysql.connector.Error as err:
            print(f"Failed to create or check database '{db_name}': {err}")

    # Attempts to create the tables if not found
    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.connection.commit()

    # Creates all the tables
    def create_tables(self):
        self.create_table("User", """
            UserID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(50) NOT NULL,
            UserType ENUM('Rider', 'Driver') NOT NULL
        """)

        self.create_table("Driver", """
            DriverID INT PRIMARY KEY,
            Driver_mode BOOLEAN NOT NULL,
            Rating FLOAT NOT NULL,
            FOREIGN KEY (DriverID) REFERENCES User (UserID)
        """)

        self.create_table("Trip", """
            TripID INT AUTO_INCREMENT PRIMARY KEY,
            RiderID INT NOT NULL,
            DriverID INT NOT NULL,
            Pickup_location VARCHAR(200) NOT NULL,
            Dropoff_location VARCHAR(200) NOT NULL,
            Fare DECIMAL(7,2) NOT NULL,
            FOREIGN KEY (RiderID) REFERENCES User (UserID),
            FOREIGN KEY (DriverID) REFERENCES Driver (DriverID)
        """)

        self.create_table("Rating", """
            RatingID INT AUTO_INCREMENT PRIMARY KEY,
            TripID INT NOT NULL,
            RiderID INT NOT NULL,
            DriverID INT NOT NULL,
            Rating_score INT NOT NULL CHECK (Rating_score BETWEEN 1 AND 5),
            FOREIGN KEY (TripID) REFERENCES Trip (TripID),
            FOREIGN KEY (RiderID) REFERENCES User (UserID),
            FOREIGN KEY (DriverID) REFERENCES Driver (DriverID)
        """)
        print("Tables created!")

    # Creates a new record for user
    def insert_user(self, user_id, name, user_type):
        query = f"INSERT INTO User (UserID, Name, UserType) VALUES ('{user_id}','{name}', '{user_type}')"
        self.add_record(query)

    # Creates a new record for driver
    def insert_driver(self, driver_id, driver_mode, rating):
        query = f"INSERT INTO Driver (DriverID, Driver_mode, Rating) VALUES ({driver_id}, {driver_mode}, {rating})"
        self.add_record(query)

    # Creates a new record for a trip
    def insert_trip(self, rider_id, driver_id, pickup_location, dropoff_location, fare):
        query = f"INSERT INTO Trip (RiderID, DriverID, Pickup_location, Dropoff_location, Fare) VALUES ({rider_id}, {driver_id}, '{pickup_location}', '{dropoff_location}', {fare})"
        self.add_record(query)
        self.cursor.execute("SELECT LAST_INSERT_ID()")
        trip_id = self.cursor.fetchone()[0]
        return trip_id

    # Rating table operations
    def insert_rating(self, trip_id, rider_id, driver_id, rating_score):
        query = f"INSERT INTO Rating (TripID, RiderID, DriverID, Rating_score) VALUES ({trip_id}, {rider_id}, {driver_id}, {rating_score})"
        self.add_record(query)

    # User table operations
    def get_user_by_id(self, user_id):
        query = f"SELECT * FROM User WHERE UserID={user_id}"
        return self.select_record(query)

    # Driver table operations
    def get_driver_by_id(self, driver_id):
        query = f"SELECT * FROM Driver WHERE DriverID={driver_id}"
        return self.select_record(query)

    # Function to update the driver mode
    def update_driver_mode(self, driver_id, new_mode):
        query = f"UPDATE Driver SET Driver_mode={new_mode} WHERE DriverID={driver_id}"
        self.add_record(query)

    # Function to get rides for a user (rider or driver)
    def get_rides_by_user(self, user_id, user_type):
        if user_type == 'Rider':
            query = f"SELECT * FROM Trip WHERE RiderID={user_id}"
        elif user_type == 'Driver':
            query = f"SELECT * FROM Trip WHERE DriverID={user_id}"
        
        return self.select_record(query)

    # Function to find an available driver
    def find_driver(self):
        query = "SELECT * FROM Driver WHERE Driver_mode=True"
        drivers = self.select_record(query)

        if drivers:
            return drivers[0]
        else:
            return None

    # Function to get the last trip by RiderID
    def get_last_trip_by_rider(self, rider_id):
        query = f"SELECT * FROM Trip WHERE RiderID={rider_id} ORDER BY TripID DESC LIMIT 1"
        return self.select_record(query)

    # Function to update the driver rating
    def update_driver_rating(self, driver_id, new_rating):
        driver = self.get_driver_by_id(driver_id)
        if driver:
            current_rating = driver[0][2]
            updated_rating = (current_rating + new_rating) / 2
            query = f"UPDATE Driver SET Rating={updated_rating} WHERE DriverID={driver_id}"
            self.add_record(query)

    def add_record(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def select_record(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    # destructor that closes connection to database
    def close(self):
        self.connection.close()

# A main to test the functions
if __name__ == '__main__':
    db_ops = db_operations("RideShare")
    db_ops.get_user_by_id(2)
    db_ops.close()
