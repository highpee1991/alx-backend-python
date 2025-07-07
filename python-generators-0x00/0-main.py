#!/usr/bin/python3

import seed

connection = seed.connect_db()
if connection: 
    seed.create_database(connection)
    print("✅ Connection successful and database created.")
    connection.close()
else:
    print("❌ Connection failed.")


# Connect to ALX_prodev database specifically
connection = seed.connect_to_prodev()

if connection:
    print("✅ Connected to ALX_prodev.")

    seed.create_table(connection)
    seed.insert_data(connection, 'user_data.csv')

    cursor = connection.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("📦 Tables in ALX_prodev:", tables)

    cursor.execute("DESCRIBE user_data;")
    schema = cursor.fetchall()
    print("\n📐 user_data Table Schema:")
    for row in schema:
            print(row)
            
    cursor.close()
    connection.close()
else:
     print("❌ Failed to connect to ALX_prodev.")



