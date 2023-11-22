#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

=======
from sqlalchemy import Column, String, Text, ForeignKey
>>>>>>> 152aebe44248f30bd531e778528fc26a7912fd85

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
<<<<<<< HEAD
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization for review"""
        super().__init__(*args, **kwargs)
=======
    #user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(Text(1024), nullable=False)
>>>>>>> 152aebe44248f30bd531e778528fc26a7912fd85
