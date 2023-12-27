#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                Column('place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False),
                Column("amenity_id", String(60),
                ForeignKey("amenities.id"),
                primary_key=True, nullable=False))


a_table = Table('place_amenity', Base.metadata,
                Column('place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False),
                Column("amenity_id", String(60),
                ForeignKey("amenities.id"),
                primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly='plave_amenity')

    if models.HBNB_TYPE_STORAGE != "db":
        @property
        def reviews(self):
            """ returns the list of Review instances with
            place_id equals to the current Place.id"""
            review_list = []
            review_instances = storage.all(Amenity)
            for i in review_instances.values():
                if i.amenity.id == self.id:
                    review_list.append(i)
            return review_list
        @property
        def amenities(self):
            """getter"""
            list_amenity = []
            amenity_ins = models.storage.all(Amenity)
            for i in amenity_ins.values():
                if i.id in self.amenity_ids:
                    list_amenity.append(i)
            return list_amenity

    reviews = relationship('Review', cascade="all,delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly='plave_amenity')


    if models.HBNB_TYPE_STORAGE != "db":
        @property
        def reviews(self):
            """ returns the list of Review instances with
            place_id equals to the current Place.id"""
            review_list = []
            review_instances = storage.all(Amenity)
            for i in review_instances.values():
                if i.amenity.id == self.id:
                    review_list.append(i)
            return review_list

        @property
        def amenities(self):
            """getter"""
            list_amenity = []
            amenity_ins = models.storage.all(Amenity)
            for i in amenity_ins.values():
                if i.id in self.amenity_ids:
                    list_amenity.append(i)
            return list_amenity

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
