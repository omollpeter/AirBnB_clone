#!/usr/bin/python3
"""
This module contains the following class definitions:
    Place: Inherits from the BaseModel (Defines a Place)

"""


from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    """
    Defines a Place class

    Public class attributes:
        city_id (str): city_id of the City (default is empty string)
        user_id (str): user_id of the User (default is empty str)
        name (str): name of the Place (default is empty str)
        description (str): description of the Place (def is empty str)
        number_rooms (int): number of rooms in the Place (default is 0)
        number_bathrooms (int): number of bathrooms in the Place (0)
        max_guest(int): max number of guest in the Place (default is 0)
        price_by_night (int): price_by_night in the Place (0)
        latitude (float): latitude of the Place (default is 0.0)
        longitude (float): longitude of the Place (default is 0.0)
        amenity_ids (list): amenity_id in the Place (default is [])
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
