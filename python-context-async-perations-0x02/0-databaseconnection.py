import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None


    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exec_type, exec_val, exec_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


with DatabaseConnection("users.db") as cursor:
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(result) 