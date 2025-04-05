import os

from dotenv import load_dotenv

load_dotenv()

TOKEN_API = os.getenv('API_TOKEN')
URL_API = os.getenv('URL_API')