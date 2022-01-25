from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

parser = ConfigParser()
parser.read('app/app.config')

user = parser.get('DB', 'User', fallback=False)
password = parser.get('DB', 'Password', fallback=False)
host = parser.get('DB', 'Host', fallback=False)
dbname = parser.get('DB', 'Dbname', fallback=False)

SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}/{dbname}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
