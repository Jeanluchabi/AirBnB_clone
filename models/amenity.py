#!/usr/bin/python3
"""Define amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The amenity's name.
    """
    name = ""
