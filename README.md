# CoinGecko Crypto ETL Pipeline

## 1. Project Description
This project is a Python-based Extract, Transform, Load (ETL) pipeline that automatically fetches live cryptocurrency price data for the top 10 coins by market cap. It extracts raw JSON data from the public CoinGecko API, transforms it into a clean, structured format, and loads it into a local DuckDB database for storage and analysis.

This pipeline was built to apply practical data engineering principles, covering API integration, data transformation, database management, error handling, retry logic, duplicate prevention, professional logging, automated testing, and Docker containerization.

## 2. Tech Stack
* **Python 3.13** — Core programming language
* **requests** — For fetching raw data from the CoinGecko REST API
* **duckdb** — Analytical database for local data storage
* **datetime** — Built-in Python library for generating run timestamps
* **logging** — Built-in Python library for recording pipeline activity
* **pytest** — For running automated unit tests
* **python-dotenv** — For loading environment variables from `.env`
* **twilio** — For sending WhatsApp price alerts
* **Docker** — For containerizing and running the pipeline consistently

## 3. Project Structure
```text
crypto_etl/
│
├── extract.py        # Fetches raw data from CoinGecko API with retry logic
├── transform.py      # Cleans and shapes raw data, selecting specific fields
├── load.py           # Loads clean data into DuckDB with duplicate prevention
├── main.py           # Orchestrates the execution of the ETL pipeline
├── config.py         # Central configuration values and constants
├── alert.py          # Sends WhatsApp alerts for significant price changes
├── test_transform.py # Automated tests for the transform logic
├── check_db.py       # Quick script to verify SQLite database contents
├── check_duckdb.py   # Quick script to verify DuckDB database contents
├── requirements.txt  # Project dependencies
├── Dockerfile        # Docker image definition
├── .dockerignore     # Files excluded from the Docker image
├── run.bat           # Script to run the containerized pipeline on Windows
├── pipeline.log      # Auto-generated log file recording pipeline runs
├── data/             # Auto-generated folder containing the DuckDB database
├── .env              # Environment variables (not tracked by Git)
├── .gitignore        # Files and folders excluded from version control
└── README.md         # Project documentation
```

## 4. How to Set It Up

### Option A: Run with Docker (Recommended)
1. **Install Docker Desktop** from https://www.docker.com

2. **Clone the repository:**
```bash
git clone https://github.com/yusufalamin001/crypto_etl.git
cd crypto_etl
```

3. **Create your `.env` file** with your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+your_number
```

4. **Build the Docker image:**
```bash
docker build -t crypto-etl:v1 .
```

5. **Run the pipeline:**
```bash
docker run --env-file .env -v /path/to/crypto_etl/data:/crypto_etl/data crypto-etl:v1
```

### Option B: Run Locally
1. **Clone the repository:**
```bash
git clone https://github.com/yusufalamin001/crypto_etl.git
cd crypto_etl
```

2. **Create and activate a virtual environment:**
   * On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
   * On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create your `.env` file** with your Twilio credentials as shown above.

## 5. How to Run It

### With Docker:
```bash
docker run --env-file .env -v /path/to/crypto_etl/data:/crypto_etl/data crypto-etl:v1
```

### Locally:
```bash
python main.py
```

This will trigger the extract, transform, and load sequence automatically, generating the `data/crypto_data.duckdb` and `pipeline.log` files on the first run.

## 6. How to Run Tests
This project includes automated tests to ensure the data transformation logic functions correctly. To run the full test suite:
```bash
pytest
```

## 7. Sample Output
When the pipeline runs successfully your terminal and `pipeline.log` file will show:
```text
2026-03-19 17:23:54,173 - INFO - Successfully transformed 10 records
2026-03-19 17:23:58,768 - INFO - Successfully loaded 10 records
```

## 8. Automated Scheduling (Windows Task Scheduler)
This pipeline is configured to run automatically on a daily schedule using Windows Task Scheduler, collecting fresh cryptocurrency data every day without manual intervention.

> **Note:** The pipeline requires your PC to be on and Docker Desktop running at the scheduled time.

To set up the schedule on your machine:

1. Open **Task Scheduler** and click **"Create Basic Task"**
2. Name it `Crypto ETL Pipeline`
3. Set the trigger to **Daily** at your preferred time
4. Set the action to **"Start a Program"**
5. In the **Program/script** field enter:
```
C:\Users\YourUsername\crypto_etl\run.bat
```
6. In the **Start in** field enter:
```
C:\Users\YourUsername\crypto_etl
```

Each daily run appends 10 new records to the database, building a historical dataset of cryptocurrency prices over time.

## 9. WhatsApp Price Alerts
This pipeline includes an automated alert system that sends a WhatsApp notification when any coin experiences a price change exceeding the configured threshold within 24 hours.

**How it works:**
- After each pipeline run the alert system checks every coin's `price_change_24h` value
- If the absolute price change exceeds the threshold a WhatsApp message is sent automatically
- Both price increases and drops trigger alerts

**Configuration:**
The alert threshold is controlled in `config.py`:
```python
PRICE_CHANGE_THRESHOLD = 5.0  # percentage
```

**Setup Requirements:**
- A free Twilio account at https://www.twilio.com
- A connected WhatsApp sandbox number
- The following environment variables in your `.env` file:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+your_number
```

**Sample Alert Message:**
```
🚨 Crypto Alert! Bitcoin has changed by 1049.60 in the last 24 hours.
Current price: $68608.0
```

## 10. Pipeline Reliability Features

### Retry Logic
The extraction step automatically retries up to 3 times with a 10 second wait between attempts if the CoinGecko API is temporarily unavailable. This ensures the pipeline handles network issues gracefully instead of failing silently.

### Duplicate Prevention
The pipeline uses a `UNIQUE(coin_name, recorded_at)` constraint on the database combined with `ON CONFLICT DO NOTHING` to ensure the same coin is never inserted twice for the same date, even if the pipeline runs multiple times in a day.
