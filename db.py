from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE=f"postgresql://postgres:1234@localhost:5432/book_store"

engine=create_engine(URL_DATABASE)

sesion_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db= sesion_local()
    try:
        yield db
        db.commit()
    finally:
        db.close()
            