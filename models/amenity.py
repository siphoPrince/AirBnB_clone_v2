#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Class definition for amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

    def __init__(self, *args, **kwargs):
        """init inherited"""
        super().__init__(*args, **kwargs)
=======
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
>>>>>>> 152aebe44248f30bd531e778528fc26a7912fd85
