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
                pattern1 = r'(\[[a-zA-Z]+\])'
                pattern3 = r'(\{.*\})'
                pattern4 = r'(datetime.datetime\([0-9, ]*\))'
                obj_cls = re.search(pattern1, value).group(1).strip("[]")
                cls_dt = re.search(pattern3, value).group(1).replace("'", '"')
                dates = re.findall(pattern4, cls_dt)
                for date in dates:
                    new_date = date
                    new_date = new_date.split("(")[1].strip(")")
                    new_date = new_date.split(", ")
                    new_date = datetime(
                        int(new_date[0]),
                        int(new_date[1]),
                        int(new_date[2]),
                        int(new_date[3]),
                        int(new_date[4]),
                        int(new_date[5]),
                        int(new_date[6])
                    )
                    new_date = new_date.isoformat()
                    cls_dt = cls_dt.replace(date, '"' + new_date + '"')
                cls_dt = json.loads(cls_dt)
                cls_dt["__class__"] = obj_cls
                dict_[key] = cls_dt
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
