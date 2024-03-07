#!/usr/bin/python3
"""
This module contains the following class definitions:
    Review: Inherits from the BaseModel (Defines a Review)

"""


from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """
    Defines a Review class

    Public class attributes:
        place_id (str): place_id of the Place (default is empty string)
        user_id (str): user_id of the User (default is empty str)
        text (str): text of the Review (default is empty str)
    """

    place_id = ""
    user_id = ""
    text = ""
