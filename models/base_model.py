#!/usr/bin/python3
"""
This module contains the following class definitions:
    BaseModel - Defines all common attributes/methods for other
                classes

The module also links BaseModel to FileStorage using storage variable

"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines a BaseModel class that defines all common attributes
    /methods for other classes

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all BaseModel instance attributes

        Args:
            args: Not used
            kwargs (dict): A dictionary to create a new instance of
                        BaseModel

        Attributes:
            id (str): Unique id for each instance
            created_at (datetime): Current time when an instance is
                                created
            updated_at (datetime): created_at time, updated everytime
                                    instance is changed
        """

        if args:
            raise TypeError("args should not be used")
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self.__class__, key, value)
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        storage.new(self.to_dict())

    def __str__(self):
        """
        Returns unofficial string representation of BaseModel
        instance
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        inst_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                inst_dict[key] = value.isoformat()
            else:
                inst_dict[key] = value
        inst_dict["__class__"] = self.__class__.__name__
        return inst_dict
