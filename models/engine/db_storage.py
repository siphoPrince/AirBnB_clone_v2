#!/usr/bin/python3
"""New engine Model"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


class DBStorage:
    """New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        
        self.__engine = create_engine((f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}'), pool_pre_ping = True)
        if HBNB_ENV == 'test':
            Box.metadata.dp_all(self.__engine)

