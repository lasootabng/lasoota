""" db_config.py"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from typing import Generator
from contextlib import contextmanager
# from src.constants import get_config
from os import environ
from dotenv import load_dotenv

load_dotenv()


# def get_connector(schema="postgres-docker"):
#     """ database connection creds """

#     config = get_config(key=schema)

#     connect_url = sqlalchemy.engine.URL.create(drivername=config['driver'],
#                                                username=config["userName"],
#                                                password=config["password"],
#                                                host=config["host"],
#                                                port=config["port"],
#                                                database=config["schema"])
#     return connect_url


engine = sqlalchemy.create_engine(environ.get("DATABASE_URL"), pool_size=10,
                                  max_overflow=2,
                                  pool_recycle=300,
                                  pool_pre_ping=True,
                                  pool_use_lifo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session_scope() -> Generator:
    """ Provide a transactional scope around a series of operations. """

    session = None
    try:
        # create session from SQLAlchemy session maker
        session = Session()
        yield session
    finally:
        session.close()


def receive_query(query):
    """ result dict formatter """
    return [row._asdict() for row in query]
