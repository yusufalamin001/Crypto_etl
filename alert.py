import logging
import os
from twilio.rest import Client
from dotenv import load_dotenv
from config import PRICE_CHANGE_THRESHOLD

load_dotenv()

def send_whatsapp_alert(coin_name, current_price, price_change):
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        
        message = f"🚨Crypto Alert! {coin_name} has changed by {price_change:.2f} in the last 24 hours. Current price: ${current_price}"
        
        client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_WHATSAPP_FROM"),
            to=os.getenv("TWILIO_WHATSAPP_TO")
        )
        logging.info(f"Alert sent for {coin_name}")
        
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")

def check_and_alert(clean_data):
    if not clean_data:
        logging.warning("No data to check for alerts")
        return
    
    for coin in clean_data:
        price_change = coin["price_change_24h"]
        if abs(price_change) > PRICE_CHANGE_THRESHOLD:
            send_whatsapp_alert(
                coin["coin_name"],
                coin["current_price"],
                price_change
            )