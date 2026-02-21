import requests
from config import API_URL
import logging

def extract():
    try:
        response=requests.get(API_URL)
        response.raise_for_status()
        raw_data=response.json()
        return raw_data
    except Exception as e:
        logging.error(f"Error extracting data: {e}")
        return []