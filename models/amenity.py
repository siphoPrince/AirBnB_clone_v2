#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
import models
from sqlalchemy import Column, String
=======
from sqlalchemy import Column, String, Integer, Float, ForeignKey
>>>>>>> 60144fb6785a88c1c4fe89bfce74db1db5f0303f
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Class definition for amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """init inherited"""
        super().__init__(*args, **kwargs)
=======
class Amenity(BaseModel, Base):
    """Class definition for amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
>>>>>>> 60144fb6785a88c1c4fe89bfce74db1db5f0303f
