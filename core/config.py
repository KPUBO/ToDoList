
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

FULL_DB_URL = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/%postgres'

APP_HOST = '127.0.0.1'
APP_PORT = 3228