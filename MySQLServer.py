import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Change this if your MySQL server is on a different host
            user="root",       # Replace with your MySQL username
            password="password"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Confirm the creation
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle database connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
