#!/usr/bin/python3
"""
This module contains the following class definitions:
    State: Inherits from the BaseModel (Defines a State)

"""


from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """
    Defines a State class

    Public class attributes:
        name (str): name of the State (default is empty string)
    """

    name = ""
