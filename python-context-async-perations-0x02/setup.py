import sqlite3
from datetime import datetime

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
)
''')

now = datetime.now().isoformat()

users = [
      ('Alice', 24, 'alice@example.com', now, now),
    ('Bob', 17, 'bob@example.com', now, now),
    ('Charlie', 19, 'charlie@example.com', now, now),
    ('David', 16, 'david@example.com', now, now),
    ('Eve', 22, 'eve@example.com', now, now)
]


cursor.executemany('INSERT INTO users (name, age, email, created_at, updated_at) VALUES (?, ?, ?, ?, ?)', users)
conn.commit()
conn.close()

print("✅ Sample users.db created with email and timestamp fields")