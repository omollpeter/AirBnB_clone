#!/usr/bin/python3
"""
This module contains the following class definitions:
    FileStorage: Serializes instances to a JSON file and deserializes JSON
                    file to instances

"""

import json
from pathlib import Path


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
        key = obj["__class__"] + "." + obj["id"]
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        path = Path(self.__file_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as obj_file:
                self.__objects = json.load(obj_file)
