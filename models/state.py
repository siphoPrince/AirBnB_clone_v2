#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __str__(self):
        """String representation of the State object."""
        return "[State] ({}) {}".format(self.id, self.__dict__)
