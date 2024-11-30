import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

# Create the users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

print("Users table created successfully!")

# Close the connection
conn.commit()
conn.close()
