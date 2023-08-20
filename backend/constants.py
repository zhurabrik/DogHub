import os
from pathlib import Path

POSTGRES_USER = os.getenv("PD_DB_USER", "postgres")
POSTGRES_PWD = os.getenv("PD_DB_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("PD_DB_HOST", "postgres")
POSTGRES_PORT = os.getenv("PD_DB_PORT", "5432")
POSTGRES_DB = os.getenv("PD_DB_NAME", "db")
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
PROJECT_PATH = Path(__file__).parent.resolve()
