from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.src.infra.config import databaseURL

engine = create_engine(databaseURL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()