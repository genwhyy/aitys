from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.environ.get("DB_NAME", "test.db")

SECRET_KEY = os.environ.get("09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
ALGORITHM = os.environ.get("ALGORITHM","HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 60))