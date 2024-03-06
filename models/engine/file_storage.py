#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """this is a representation of a class.

    Attributes:
        it contains two attributes file path and objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """a function that returns all functions in storage."""
        return FileStorage.__objects

    def new(self, obj):
        """a function that returns the new file."""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_class_name}.{obj.id}"] = obj

    def save(self):
        """a function that is used to save a file."""
        objects_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """a function for the purpose of reloading a file.."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
