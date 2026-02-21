import sqlite3
from config import DATABASE_NAME, TABLE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()