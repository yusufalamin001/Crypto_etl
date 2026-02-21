import logging
from extract import extract
from transform import transform
from load import load


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("pipeline.log")
    ]
)

def main():
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

if __name__ == "__main__":
    main()