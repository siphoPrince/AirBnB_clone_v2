#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class definition for amenity"""
    __tablename__ = 'amenities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")


def __init__(self, *args, **kwargs):
        """init inherited"""
        super().__init__(*args, **kwargs)
