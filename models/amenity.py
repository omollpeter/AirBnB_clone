#!/usr/bin/python3
"""
This module contains the following class definitions:
    Amenity: Inherits from the BaseModel (Defines a Amenity)

"""


from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """
    Defines a Amenity class

    Public class attributes:
        name (str): name of the Amenity (default is empty string)
    """

    name = ""
