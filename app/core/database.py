from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", ".env")
print('dotnev path')
print(dotenv_path)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", ".env"))

DATABASE_URL = os.getenv("DATABASE_URL", "ACHUT",)
DB_NAME = os.getenv('DATABASE_NAME', "ACHOU FOI NADA")
print("DB_NAME")
print(DB_NAME)

engine = create_engine(DATABASE_URL )
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()