#!/usr/bin/python3
"""a code Module containing the BaseModel class."""
import models
import json
import csv
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """base model functionality in its class."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.
            arguments :id, save, string etc.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary containing all keys/values."""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """string function"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """ update datetime function"""
        self.updated_at = datetime.today()
        models.storage.save()
