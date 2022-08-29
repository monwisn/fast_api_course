import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://gczclietwxqbps:4451f95c650fa6ad6c43d4a11fed44622f86c1b7b6e75f088a450f04a8fb2d00@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d46ai6t7ce0p8l"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
