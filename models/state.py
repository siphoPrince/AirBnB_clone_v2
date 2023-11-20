#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State cass """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",backref="state")

    @properties
    def cities(self):
        """returns the list of City instances """
        C_list = []
        city_instances = storage.all(City)
        for instance in city_instances.values():
            if instance.state_id == self.id:
                C_list.append(instance)
        return C_list

    def __str__(self):
        """String representation of the State object."""
        return "[State] ({}) {}".format(self.id, self.__dict__)
