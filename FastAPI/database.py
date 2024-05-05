# create_engine function creates an engine that will interface with the database
# creates and manages db connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sets up db file called finance.db within our local repository
URL_DATABASE = 'sqlite:///./finance.db'

# connect_args... allows db to be accessed from multi threads (web apps built using fastapi)
# this is specific to SQLITE only
engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

