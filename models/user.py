#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.review import Review
>>>>>>> 152aebe44248f30bd531e778528fc26a7912fd85
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    places = relationship('Place', backref='user', cascade='delete')
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """ init of User"""
        super().__init__(*args, **kwargs)
=======

>>>>>>> 152aebe44248f30bd531e778528fc26a7912fd85
