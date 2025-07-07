import mysql.connector
from mysql.connector import Error
import csv
import uuid

# ////////
def connect_db(): 
    #  """Connect to the MySQL server (without selecting a database)."""
    try:
        connection = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            password= 'oluwaseun1991'
        )
        return connection 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
    

# ///////////
def create_database(connection): 
    #  """Create the ALX_prodev database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("alxprodev database created or already exist")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")

# Connect specifically to the ALX_prodev database
def connect_to_prodev():
    try: 
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='oluwaseun1991',
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None
    

# Create the user_data table
def create_table(connection): 
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age INT NOT NULL
            )
        ''')
        connection.commit()
        print("✅ Table user_data created successfully")
        cursor.close()
    except Error as e: 
        print(f"Error creating table: {e}")




def insert_data(connection, csv_path):
    try:
        cursor = connection.cursor()

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0

            for row in reader:
                # generate uuid for each user
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = int(row['age'])

                # insert into database
                cursor.execute('''
                               INSERT INTO user_data (user_id, name, email, age)
                               VALUES (%s, %s, %s, %s)
                               ''', (user_id, name, email, age))
                count += 1
        
        connection.commit()
        print(f"✅ Data inserted successfully from CSV. Total rows: {count}")
        cursor.close()
    except Error as e:
        print("Error inserting data: {e}")

    