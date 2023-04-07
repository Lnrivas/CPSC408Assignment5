from db_operations import db_operations

def rider_menu(user_id, db):
    while True:
        print("\nRider Menu:")
        print("1. View Rides")
        print("2. Find a Driver")
        print("3. Rate My Driver")
        print("4. Logout")
        option = input("Choose an option: ")

        if option == '1':
            rides = db.get_rides_by_user(user_id, "Rider")
            for ride in rides:
                print("Ride ID:", ride[0], "Pickup:", ride[3], "Dropoff:", ride[4])

        elif option == '2':
            driver = db.find_driver()
            if driver:
                print("Found a driver! Driver ID:", driver[0])
                pickup_location = input("Enter pickup location: ")
                dropoff_location = input("Enter dropoff location: ")
                fare = float(input("Enter fare: "))
                db.insert_trip(user_id, driver[0], pickup_location, dropoff_location, fare)
                print("Ride created successfully.")
            else:
                print("No drivers are available at the moment.")

        elif option == '3':
            last_trip = db.get_last_trip_by_rider(user_id)
            if last_trip:
                print("Last ride information:")
                print("Ride ID:", last_trip[0][0], "Driver ID:", last_trip[0][2])
                correct_ride = input("Is this the correct ride? (yes/no): ")
                if correct_ride.lower() == 'yes':
                    new_rating = int(input("Enter your rating (1-5): "))
                    db.update_driver_rating(last_trip[0][2], new_rating)
                    print("Rating updated successfully.")
                else:
                    print("Please contact support to rate a different ride.")
            else:
                print("No rides found.")

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

        if option == '1':
            driver = db.get_driver_by_id(user_id)
            if driver:
                print("Your current rating is:", driver[0][2])

        elif option == '2':
            rides = db.get_rides_by_user(user_id, "Driver")
            for ride in rides:
                print("Ride ID:", ride[0], "Pickup:", ride[3], "Dropoff:", ride[4])

        elif option == '3':
            driver = db.get_driver_by_id(user_id)
            if driver:
                new_mode = not driver[0][1]
                db.update_driver_mode(user_id, new_mode)
                print("Driver mode updated.")
            else:
                print("Driver not found.")

        elif option == '4':
            break

        else:
            print("Invalid option. Please try again.")


def main():
    db = db_operations("RideShare")
    db.create_tables()

    while True:
        print("\nWelcome to Rideshare!")
        print("1. New User")
        print("2. Returning User")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == '1':
            user_id = input("Enter id: ")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user_type = input("Enter user type (Rider/Driver): ")

            if user_type.lower() == 'rider':
                db.insert_user(user_id, name, email, password, 'Rider')
            elif user_type.lower() == 'driver':
                db.insert_user(user_id, name, email, password, 'Driver')
                db.insert_driver(user_id, False, 5)

            print(f"User created successfully. Your user ID is {user_id}.")

        elif option == '2':
            user_id = int(input("Enter your user ID: "))
            user = db.get_user_by_id(user_id)
            if user:
                user_type = user[0][4]
                if user_type == 'Rider':
                    rider_menu(user_id, db)
                elif user_type == 'Driver':
                    driver_menu(user_id, db)
            else:
                print("User not found. Please try again.")

        elif option == '3':
            break

        else:
            print("Invalid option. Please try again.")

    db.close()

if __name__ == "__main__":
    main()
