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

    classes =["State", "City", "User", "Place", "Review"]

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

    def all(self, cls=None):
        """return dictionary"""
        dict_db = {}

        if cls == None:
            for clas in self.classes:
                #clas = eval(clas)
                query = self.__session.query(clas).all()
                print(query)
                for instance in query:
                    key = instance.__class__.__name__ + '.' + instance.id
                    dict_db[key] = instance
        else:
            query = self.__session.query(cls).all()
            for instance in query:
                key = instance.__class__.__name__ + '.' + instance.id
                dict_db[key] = instance
        
        return dict_db

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """ends session"""
        self.reload()
        self.__session.close()


