import requests
from config import API_URL
import logging
import time

def extract():
    for attempt in range(3):
        try:
            response=requests.get(API_URL)
            response.raise_for_status()
            raw_data=response.json()
            return raw_data
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed, retrying...: {e}")
            time.sleep(10)
    logging.error("Extraction failed")
    return []