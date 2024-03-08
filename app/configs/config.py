
import os 
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", None),
    "port": os.getenv("DB_PORT", None),
    "user": os.getenv("DB_USER", None),
    "password": os.getenv("DB_PASSWORD", None),
    "database": os.getenv("DB_NAME", None)
}

SERVER_PORT = eval(os.getenv("SERVER_PORT", "8000"))
SERVER_HOST = os.getenv("SERVER_HOST", "")