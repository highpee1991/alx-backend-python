import mysql.connector
from mysql.connector import Error

def stream_data():
    try:
        connection = mysql.connector.connect(
           host='localhost',
           user='root',
           password='oluwaseun1991',
           database='ALX_prodev'
           )
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        # This part makes it a generator: yield one row at a time
        for row in cursor:
            yield row


    except Error as e:
       print(f"Error: {e}")

    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

                    

if __name__ == "__main__":
    for record in stream_data():
        print(record)