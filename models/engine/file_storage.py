#!/usr/bin/python3
"""
This module contains the following class definitions:
    FileStorage: Serializes instances to a JSON file and deserializes JSON
                    file to instances

"""

import json
from pathlib import Path
import re
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON
    file to instances

    Private class attributes:
        file_path (str): Path to the JSON file
        objects (dict): Stores all objects by id
    """

    __file_path = "file.json"
    __objects = {}
    # __objects_dict = {}

    def all(self):
        """
        Returns all objects
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel instance): Instance of BaseModel
        """
        obj_id = obj.id
        obj_cls = obj.__class__.__name__
        key = obj_cls + "." + obj_id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict_ = {}
            for key, value in self.__objects.items():
                dict_[key] = value.to_dict()
            json.dump(dict_, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State
        path = Path(self.__file_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as obj_file:
                self.__objects = {}
                objs_in_file = json.load(obj_file)
                for key, value in objs_in_file.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(f"{cls_name}(**value)")

    def get_path(self):
        """
        Retrieves file storage path
        """
        return self.__file_path
