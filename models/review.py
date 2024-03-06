#!/usr/bin/python3
"""This code defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Representation of a review and the attributes involved.

    Attributes:
        place_id (str).
        user_id (str).
        text (str).
    """

    place_id = ""
    user_id = ""
    text = ""
