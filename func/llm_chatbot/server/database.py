from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///dev.db")
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

