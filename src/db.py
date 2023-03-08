from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
port = config.get('DB', 'port')

url = f'postgresql://{username}:{password}@{domain}:{port}/{db_name}'
Base = declarative_base()
engine = create_engine(url, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()



