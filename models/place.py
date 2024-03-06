#!/usr/bin/python3
"""This code defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """shows a representation of a place and its attributes.

    Attributes:
        city_id (str).
        user_id (str).
        name (str).
        description (str).
        number_rooms (int).
        number_bathrooms (int).
        max_guest (int).
        price_by_night (int).
        latitude (float).
        longitude (float).
        amenity_ids (list).
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
