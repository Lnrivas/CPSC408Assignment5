from helper import helper
from db_operations import db_operations

db_ops = db_operations()

# db_ops.create_user_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_driver_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_trip_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_rating_table() # RUN ONLY ONCE, THEN COMMENT OUT

def start_screen():
    print("Welcome to the RideShare app!")

# gets user input for which type of user they are (new user or returning user)
def user_type_selection():
    print('''Select the type of user you are:
    1. New user
    2. Returning user
    ''')
    return helper.get_choice([1,2])

# gets user input for which account type to create (rider account or driver account)
def account_type_selection():
    print('''Select the type of account you want to make:
    1. Create rider account
    2. Create driver account
    ''')
    return helper.get_choice([1,2])

# creates a rider account
def create_rider_account():
    print("making rider account")
    userID = input("Enter a new user ID (must be an integer): ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    userType = "Rider"
    query = f"INSERT INTO User VALUES({userID},'{name}','{email}','{password}','{userType}');"
    db_ops.add_record(query)

# creates a driver account
def create_driver_account(): 
    print("making driver account")
    userID = input("Enter a new user ID (must be an integer): ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    userType = "Driver"
    query = f"INSERT INTO User VALUES({userID},'{name}','{email}','{password}','{userType}');"
    db_ops.add_record(query)

# gets user input for their userID and determines if they are a rider or a driver
def determine_user_type():
    userID = input("Enter your user ID: ") # INCOMPLETE METHOD

# main program
start_screen()
user_type = user_type_selection()
if user_type == 1:
    print("You are a new user")
    account_type = account_type_selection()
    if account_type == 1:
        create_rider_account()
    if account_type == 2:
        create_driver_account()
if user_type == 2:
    print("You are a returning user")
    determine_user_type()



# deconstruct at end
db_ops.destructor()
