import mysql.connector

def import_sql_file(username, password, database_name, sql_file_path):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=username,
            password=password
        )

        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")

        with open(sql_file_path, "r") as sql_file:
            sql_commands = sql_file.read().split(';')
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)

        connection.commit()

    except mysql.connector.Error as error:
        print(f"Error importing SQL file: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()