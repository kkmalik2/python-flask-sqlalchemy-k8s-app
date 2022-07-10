from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import os
# import logging
# log_file=os.getenv('LOG_FILE_PATH')
# logging.basicConfig(filename=log_file, filemode='a+', format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def create_db_engine():
    database_type = os.getenv('DATABASE_TYPE')
    database_location = os.getenv('DATABASE_LOCATION')
    print (database_type)
    print (database_location)
    # logger.info(f"engine will be created at - {database_type}:///{database_location}")
    engine = create_engine(f'{database_type}:///{database_location}', echo = True, connect_args={'check_same_thread': False})
    # logger.info(f"engine created - {database_type}:///{database_location}")
    # engine = create_engine('sqlite:///user-pref.db', echo = True, connect_args={'check_same_thread': False})
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session