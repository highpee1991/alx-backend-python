import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None 
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


with ExecuteQuery("users.db", "SELECT * FROM users WHERE age > ?", (25,)) as result:
    print(result)