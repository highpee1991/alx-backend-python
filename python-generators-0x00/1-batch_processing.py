import mysql.connector 
from mysql.connector import Error

def stream_users_in_batches(batch_size):
    #  """Yield batches of users from the database."""
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'oluwaseun1991',
            database = 'ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM user_data')

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except Error as e:
        print(f'Error: {e}')
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass



def batch_processing(batch_size):
    # """Process each batch, filter users over age 25, and print them."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)