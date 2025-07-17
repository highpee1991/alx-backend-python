import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users-db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper


def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f'transaction failed {e}')
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, user_email):
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET email = ? WHERE id=? ', (user_email, user_id))
    print(f'{cursor.rowcount} row(s) updated')

update_user_email(user_id=1, user_email='Crawford_Cartwright@hotmail.com')