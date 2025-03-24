import os

from dotenv import load_dotenv

load_dotenv()

TOKEN_API = os.getenv('API_TOKEN')
URL_API = os.getenv('URL_API')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
