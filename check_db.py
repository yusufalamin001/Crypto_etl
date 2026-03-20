import sqlite3

conn = sqlite3.connect("crypto_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM coin_prices")
rows = cursor.fetchall()

for row in rows:
    print(row)
print(f"Total records: {len(rows)}")

conn.close()