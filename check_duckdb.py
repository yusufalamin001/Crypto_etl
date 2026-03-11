import duckdb
from config import DATABASE_NAME, TABLE_NAME

conn = duckdb.connect(DATABASE_NAME)

rows = conn.execute(f"SELECT * FROM {TABLE_NAME}").fetchall()

for row in rows:
    print(row)
print(f"Total records: {len(rows)}") 


conn.close()