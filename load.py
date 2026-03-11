import duckdb
from config import DATABASE_NAME, TABLE_NAME
import logging


def load(clean_data):
    if not clean_data:
        logging.warning("No data to load - transform may have failed")
        return

    conn = duckdb.connect(DATABASE_NAME)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            coin_name TEXT,
            current_price DOUBLE,
            price_change_24h DOUBLE,
            recorded_at TEXT
        )
    """)

    for coin in clean_data:
        conn.execute(f"""
            INSERT INTO {TABLE_NAME} (coin_name, current_price, price_change_24h, recorded_at)
            VALUES (?, ?, ?, ?)
        """, (coin["coin_name"], coin["current_price"], coin["price_change_24h"], coin["recorded_at"]))

    conn.close()
    logging.info(f"Successfully loaded {len(clean_data)} records")