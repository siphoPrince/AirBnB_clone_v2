#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if models.HBNB_TYPE_STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ''

        @property
        def cities(self):
            """ getter """
            city_list = []
            city_intances = storage.all(City)
            for i in city_instances.values():
                if i.state_id == self.id:
                    city_list.append(i)
            return city_list

