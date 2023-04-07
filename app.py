from db_operations import db_operations

def rider_menu(user_id, db):
    
    while True:
        print("\nRider Menu:")
        print("1. View Rides")
        print("2. Find a Driver")
        print("3. Rate My Driver")
        print("4. Logout")
        option = input("Choose an option: ")
        
        # View Rides
        if option == '1':
            rides = db.get_rides_by_user(user_id, "Rider")
            if rides:
                for ride in rides:
                    print("Ride ID:", ride[0], "Pickup:", ride[3], "Dropoff:", ride[4])
            else:
                print("No rides found.")

        # Find a Driver
        elif option == '2':

            driver = db.find_driver()
            if driver:
                print("Found a driver! Driver ID:", driver[0])
                pickup_location = input("Enter pickup location: ")
                dropoff_location = input("Enter dropoff location: ")
                fare = float(input("Enter fare: "))

                trip_id = db.insert_trip(user_id, driver[0], pickup_location, dropoff_location, fare)
                print("Ride created successfully. Your Trip ID is:", trip_id)

            else:
                print("No drivers are available at the moment.")

        # Rate My Driver
        elif option == '3':

            last_trip = db.get_last_trip_by_rider(user_id)

            if last_trip:
                print("Last ride information:")
                print("Ride ID:", last_trip[0][0], "Driver ID:", last_trip[0][2],
                      "Pickup Location:", last_trip[0][3], "Dropoff Location:", last_trip[0][4],
                      "Fare:", last_trip[0][5])
                correct_ride = input("Is this the correct ride? (yes/no): ")

                if correct_ride.lower() == 'yes':
                    new_rating = int(input("Enter your rating (1-5): "))
                    db.update_driver_rating(last_trip[0][2], new_rating)
                    print("Rating updated successfully.")

                else:
                    print("please contact support to rate a different ride.")

            else:
                print("No rides found.")

        # Logout 
        elif option == '4':
            break

        else:
            print("Invalid option. Please try again.")

def driver_menu(user_id, db):

    while True:
        print("\nDriver Menu:")
        print("1. View Rating")
        print("2. View Rides")
        print("3. Activate/Deactivate Driver Mode")
        print("4. Logout")
        option = input("Choose an option: ")

        # View Rating
        if option == '1':
            driver = db.get_driver_by_id(user_id)
            if driver:
                print("Your current rating is:", driver[0][2])

        # View Rides
        elif option == '2':
            rides = db.get_rides_by_user(user_id, "Driver")
            if rides:
                for ride in rides:
                    print("Ride ID:", ride[0], "Pickup:", ride[3], "Dropoff:", ride[4])
            else:
                print("You do not have any rides")

        # Toggle Driver Mode
        elif option == '3':
            driver = db.get_driver_by_id(user_id)
            if driver:
                new_mode = not driver[0][1]
                db.update_driver_mode(user_id, new_mode)
                print(f"Driver Mode Updated To: {new_mode}")
            else:
                print("Driver not found.")

        # Logout
        elif option == '4':
            break

        else:
            print("Invalid option. Please try again.")

def main(user, password):

    db = db_operations("RideShare", user, password)

    while True:
        print("\nWelcome to Rideshare!")
        print("1. New User")
        print("2. Returning User")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == '1':

            user_id_exists = True

            while user_id_exists:

                user_id = input("Enter User ID: ")
                name = input("Enter your name: ")
                user_type = input("Enter user type (Rider/Driver): ")

                user = db.get_user_by_id(user_id)

                if user:
                    print("User ID already exists. Please try again with a different User ID.")
                else:
                    user_id_exists = False
                    if user_type.lower() == 'rider':
                        db.insert_user(user_id, name, 'Rider')
                    elif user_type.lower() == 'driver':
                        db.insert_user(user_id, name, 'Driver')
                        db.insert_driver(user_id, False, 5)

                    print(f"\nUser created successfully. Your user ID is {user_id}.")

        elif option == '2':
            user_id = int(input("Enter your user ID: "))
            user = db.get_user_by_id(user_id)
            if user:
               
                print("\nUser ID:", user[0][0])
                print("Name:", user[0][1])

                user_type = user[0][2]
                if user_type == 'Rider':
                    rider_menu(user_id, db)
                elif user_type == 'Driver':
                    driver_menu(user_id, db)
            else:
                print("\nUser not found. Please try again.")

        elif option == '3':
            break

        else:
            print("Invalid option. Please try again.")

    db.close()

if __name__ == "__main__":
    user = "root"
    password = "password"
    main(user, password)
