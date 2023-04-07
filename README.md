# RideShare

RideShare is a simple command-line based ride-sharing application that allows users to register as riders or drivers, and manage trips.

## Requirements

- Python 3.6 or higher
- MySQL
- `mysql-connector-python` package

## Installation

1. Clone the repository or download the source code.
2. Install the required package using the following command:

```sh
pip install mysql-connector-pytho
```

## Setup
1. Set up a MySQL server, create a user with a password and grant them necessary privileges to create, modify and delete databases.
2. Update the user and password variables in the main function in app.py with your MySQL user and password.
3. Load the rideshare_dump.sql file into your MySQL server to import the schema and populate the database.

## Running the Application
To run the application, navigate to the directory where the source code is located and run the following command:
```sh
python app.py
```