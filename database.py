import sqlite3
from datetime import datetime

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    joined_at TEXT
)
""")

conn.commit()

def add_user(uid, name):
    cur.execute(
        "INSERT OR IGNORE INTO users VALUES (?, ?, ?)",
        (uid, name, datetime.now().isoformat())
    )
    conn.commit()

def get_all_users():
    cur.execute("SELECT user_id FROM users")
    return [row[0] for row in cur.fetchall()]

def total_users():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]
