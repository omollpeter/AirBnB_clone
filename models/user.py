#!/usr/bin/python3
"""
This module contains the following class definitions:
    User: Inherits from the BaseModel (Defines a user)

"""


from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """
    Defines a User class

    Public class attributes:
        email (str): Email of the user (default is empty string)
        password (str): password of the user (default is empty str)
        first_name (str): First name of the user (default is empty str)
        last_name (str): Last name of the user (default is empty str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
