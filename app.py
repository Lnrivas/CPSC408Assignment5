from helper import helper
from db_operations import db_operations

db_ops = db_operations()

# db_ops.create_user_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_driver_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_vehicle_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_trip_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_rating_table() # RUN ONLY ONCE, THEN COMMENT OUT

def start_screen():
    print("Welcome to the RideShare app!")

def user_type_selection():
    print('''Select the type of user you are:
    1. New user
    2. Returning user
    ''')
    return helper.get_choice([1,2])

# main program
start_screen()

user_type = user_type_selection()
if user_type == 1:
    print("You are a new user")
if user_type == 2:
    print("You are a returning user")


# deconstruct at end
db_ops.destructor()
