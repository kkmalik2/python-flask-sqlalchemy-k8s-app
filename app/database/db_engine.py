from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

def create_db_engine():
    engine = create_engine('sqlite:///user-pref.db', echo = True, connect_args={'check_same_thread': False})
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session