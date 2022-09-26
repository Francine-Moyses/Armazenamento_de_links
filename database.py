import sqlite3

conn = sqlite3.connect('enterprise.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE lista (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        link TEXT NOT NULL
    );
""")
