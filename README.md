# CoinGecko Crypto ETL Pipeline

## 1. Project Description
This project is a Python-based Extract, Transform, Load (ETL) pipeline that automatically fetches live cryptocurrency price data for the top 10 coins by market cap. It extracts raw JSON data from the public CoinGecko API, transforms it into a clean, structured format, and loads it into a local SQLite database for storage and analysis.

This pipeline was built to apply practical data engineering principles, covering API integration, data transformation, database management, error handling, professional logging, and automated testing.

## 2. Tech Stack
* **Python 3.13** — Core programming language
* **requests** — For fetching raw data from the CoinGecko REST API
* **sqlite3** — Built-in Python library for local database storage
* **datetime** — Built-in Python library for generating run timestamps
* **logging** — Built-in Python library for recording pipeline activity
* **pytest** — For running automated unit tests
* **pandas** — Installed as a dependency for future data manipulation and analysis

## 3. Project Structure
```text
crypto_etl/
│
├── extract.py        # Fetches raw data from CoinGecko API
├── transform.py      # Cleans and shapes raw data, selecting specific fields
├── load.py           # Loads clean data into the SQLite database
├── main.py           # Orchestrates the execution of the ETL pipeline
├── config.py         # Central configuration values and constants
├── test_transform.py # Automated tests for the transform logic
├── check_db.py       # Quick script to verify database contents
├── requirements.txt  # Project dependencies
├── pipeline.log      # Auto-generated log file recording pipeline runs
├── crypto_data.db    # Auto-generated SQLite database for storage
├── .env              # Environment variables
├── .gitignore        # Files and folders excluded from version control
└── README.md         # Project documentation
```

## 4. How to Set It Up
To run this project locally, follow these steps:

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

## 5. How to Run It
Once your environment is set up and activated, run the pipeline with:
```bash
python main.py
```
This will trigger the extract, transform, and load sequence automatically, generating the `crypto_data.db` and `pipeline.log` files on the first run.

## 6. How to Run Tests
This project includes automated tests to ensure the data transformation logic functions correctly. To run the full test suite:
```bash
pytest
```

## 7. Sample Output
When the pipeline runs successfully your terminal and `pipeline.log` file will show:
```text
2026-02-21 18:49:10,993 - INFO - Successfully transformed 10 records
2026-02-21 18:49:11,019 - INFO - Successfully loaded 10 records
```

## 8. Automated Scheduling (Windows Task Scheduler)
This pipeline is configured to run automatically on a daily schedule using Windows Task Scheduler, collecting fresh cryptocurrency data every day without manual intervention.

To set up the schedule on your machine:

1. Open **Task Scheduler** and click **"Create Basic Task"**
2. Name it `Crypto ETL Pipeline`
3. Set the trigger to **Daily** at your preferred time
4. Set the action to **"Start a Program"**
5. In the Program/script field enter the path to your virtual environment Python executable:
```
   C:\Users\YourUsername\crypto_etl\venv\Scripts\python.exe
```
6. In the "Add arguments" field enter:
```
   main.py
```
7. In the "Start in" field enter your project folder path:
```
   C:\Users\YourUsername\crypto_etl
```

Each daily run appends 10 new records to the database, building a historical dataset of cryptocurrency prices over time.
