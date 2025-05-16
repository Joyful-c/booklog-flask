import sqlite3

conn = sqlite3.connect("books.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    memo TEXT
)
""")
conn.commit()
conn.close()
