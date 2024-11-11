import mysql.connector
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, database_name, user_name, password):
        try:
            # Establish the connection to the MySQL database
            self.connection = mysql.connector.connect(
                host='localhost',  # Update with your MySQL host
                database=database_name,  # The name of your database
                user=user_name,  # Your MySQL username
                password=password  # Your MySQL password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(buffered=True)
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None

    def query(self, sql, params=()):
        """Executes a query and commits changes if necessary."""
        print(sql, params)
        try:
            self.cursor.execute(sql, params)
            if sql.strip().lower().startswith("select"):
                result = self.cursor.fetchall()
                return result
            else:
                self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        """Closes the database connection."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed")

