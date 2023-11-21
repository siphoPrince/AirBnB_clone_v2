#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
import sqlalchemy

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True )
    created_at = Column(DateTime, default=datetime.utcnow(),nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())

        else:
            for i, j in kwargs.items():
                if i in ("created_at", "updated_at"):
                    j = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in i:
                    setattr(self, i, j)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)


    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = vars(self).copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary = {}
        dictionary.update(self.__dict__)
        try:
            del dictionary['_sa_instance_state']
        except Exception:
            pass

        dictionary.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete the current instance from the storage """
        models.storage.delete(self)
