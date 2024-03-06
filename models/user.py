#!/usr/bin/python3
"""This code Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent the actual User.

    Attributes:
        email.
        password.
        first_name.
        last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
