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
        self.__objects[key] = obj.__str__()

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict_ = {}
            for key, value in self.__objects.items():
                new_value = value.split("{")[1][:-1].replace("'", "\"")
                obj_cls = value.split("]")[0].strip("[")

                inner_dict = {}
                all_items = new_value.split(", \"")
                for value in all_items:
                    pair = value.split(": ")
                    key_ = pair[0].strip('"')
                    val_ = pair[1].strip('"')
                    if key_ == "created_at" or key_ == "updated_at":
                        val_ = val_.split("(")[1].strip(")")
                        val_ = val_.split(", ")
                        val_ = datetime(
                            int(val_[0]),
                            int(val_[1]),
                            int(val_[2]),
                            int(val_[3]),
                            int(val_[4]),
                            int(val_[5]),
                            int(val_[6])
                        )
                        val_ = val_.isoformat()
                    inner_dict[key_] = val_
                inner_dict["__class__"] = obj_cls
                dict_[key] = inner_dict
            json.dump(dict_, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        path = Path(self.__file_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as obj_file:
                dict_ = json.load(obj_file)
                obj_dicts = {}
                for key, value in dict_.items():
                    inner_dict = {}
                    for key_, val_ in value.items():
                        if key_ == "created_at" or key_ == "updated_at":
                            val_ = datetime.strptime(
                                val_, "%Y-%m-%dT%H:%M:%S.%f"
                            )
                        if key_ == "__class__":
                            continue
                        inner_dict[key_] = val_
                    obj_desc = "[{}] ({}) {}".format(
                        dict_[key]["__class__"],
                        inner_dict["id"],
                        inner_dict
                    )
                    obj_dicts[key] = obj_desc
                self.__objects = obj_dicts

    def update_objects(self, dict_):
        """
        Updates __objects with new instances
        """

        self.__objects = dict_

    def get_path(self):
        """
        Retrieves file storage path
        """
        return self.__file_path
