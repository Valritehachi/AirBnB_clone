#!/usr/bin/python3
"""This code defines the State class."""
from models.base_model import BaseModel


class City(BaseModel):
    """It represent a city with the following attributes.

    Attributes:
        name.
        state_id
    """
    state_id = ""
    name = ""
