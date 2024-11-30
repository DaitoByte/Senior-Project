import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table for storing chat messages
cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        message TEXT NOT NULL
    )
""")
conn.commit()
conn.close()
