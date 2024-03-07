#!/usr/bin/python3
"""
This module contains the following class definitions:
    City: Inherits from the BaseModel (Defines a City)

"""


from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """
    Defines a City class

    Public class attributes:
        state_id (str): state_id of the City (default is empty string)
        name (str): name of the City (default is empty str)
    """

    state_id = ""
    name = ""
