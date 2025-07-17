import sqlite3
import functools
from datetime import datetime

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query is None and args:
            query = args[0]
        if query is None:
            raise ValueError('No SQL Value Was Provided to The Function')

        print(f'[{datetime.now()}] Executing SQL Query: {query}')
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Result: {result}")
        return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
    

users = fetch_all_users(query='SELECT * FROM users')