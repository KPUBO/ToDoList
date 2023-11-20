
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

FULL_DB_URL = 'postgresql+asyncpg://postgres:1@192.168.109.145:5432/to_do_list'

APP_HOST = '0.0.0.0'
APP_PORT = 8200