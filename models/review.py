#!/usr/bin/python3
""" Review module for the HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Review(BaseModel, Base):
    """Class definition for Review"""
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(1024), nullable=False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
