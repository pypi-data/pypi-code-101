"""Constants for the package."""
import os

# Stocks DB
DB_KWARGS = {
    "dialect": "postgresql",
    "user": os.getenv("STOCKS_USER"),
    "password": os.getenv("STOCKS_PASS"),
    "host": "stock-data-postgres",
    "port": 5432,
    "db": "stocks",
}

# Stocks API Key
STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")

# List of stocks to get
STOCKS_LS = os.getenv("STOCKS_LS").split(",")

# Path to the container directory where staging data is going to be stored
PATH = "/opt/airflow/tmp_data"
