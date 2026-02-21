from datetime import datetime
import logging

def transform(raw_data):
    if not raw_data:
        logging.warning("No data to transform - extract may have failed")
        return []
    
    clean_data = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin in raw_data:
        clean_coin = {
            "coin_name": coin["name"],
            "current_price": coin["current_price"],
            "price_change_24h": coin["price_change_24h"],
            "recorded_at": timestamp
        }

        clean_data.append(clean_coin)
    logging.info(f"Successfully transformed {len(clean_data)} records")
    return clean_data