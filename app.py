from db_operations import db_operations

db_ops = db_operations()

# db_ops.create_user_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_driver_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_vehicle_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_trip_table() # RUN ONLY ONCE, THEN COMMENT OUT
# db_ops.create_rating_table() # RUN ONLY ONCE, THEN COMMENT OUT

# deconstruct at end
db_ops.destructor()
