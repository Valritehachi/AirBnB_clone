#!/usr/bin/python3
"""Module containing the BaseModel class"""
import json
import csv
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """class base for object management."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            id (int): The identifier for the instance. If not provided,
                      a unique identifier will be assigned.
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == '_created_at' or key == '_updated_at':
                    value = datetime.fromisoformat(value)

                self.__setattr__(key, value)
        else:
            self._id = str(uuid4())
            self._created_at = datetime.now()
            self._updated_at = datetime.now()

    @property
    def id(self):
        """Getter method for the 'id' attribute."""
        return self._id

    @id.setter
    def id(self, value):
        """setter method for id attribute"""
        self.validate_type('id', value)
        self.validate_xy('id', value)

        self.__id = value

    @property
    def updated_at(self):
        """Getter method for the 'id' attribute."""
        return self._updated_at

    @property
    def created_at(self):
        """Getter method for the 'id' attribute."""
        return self._created_at

    def __str__(self):
        """string function"""
        return(f"{[self.__class__.__name__]} {(self._id)} {self.__dict__}")

    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['_created_at'] = dictionary['_created_at'].isoformat()
        dictionary['_updated_at'] = dictionary['_updated_at'].isoformat()
        return dictionary

    def save(self):
        """ update datetime function"""
        from . import storage
        self._updated_at = datetime.now()

        storage.new(self)
        storage.save()
