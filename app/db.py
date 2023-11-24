from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os


DATABASE_URL = os.getenv("DATABASE_URL")
engine       = create_engine(DATABASE_URL)
Base         = declarative_base()
Session      = sessionmaker(bind=engine)