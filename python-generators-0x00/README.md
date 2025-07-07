# 🌀 Python Generators - Task 0: Getting Started

This task demonstrates how to work with **Python generators** by streaming rows from a MySQL database one at a time.

## 🛠️ Project Overview

We implemented a generator that connects to a MySQL database, reads data from a CSV file, inserts it into a table, and streams the data row by row using a generator function.

## 📂 Files

- `seed.py` – contains all database operations:
  - `connect_db()` – connects to MySQL server.
  - `create_database(connection)` – creates `ALX_prodev` database.
  - `connect_to_prodev()` – connects to the `ALX_prodev` database.
  - `create_table(connection)` – creates the `user_data` table.
  - `insert_data(connection, csv_path)` – loads and inserts data from a CSV file into the table.
- `0-main.py` – runs and tests the database setup and confirms data was inserted.

- `1-stream.py` – defines a generator:
  - `stream_data()` – yields one row at a time from the `user_data` table.

## 🧪 How to Run

> Ensure MySQL is installed and running on your machine.

1. Seed the database:

```bash
python 0-main.py
```
