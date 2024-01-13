#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Attributes:
        place_id (str): The ID of the Place .
        user_id (str): The ID of the User .
        text (str): The text of reviewing.
    """
    place_id = ""
    user_id = ""
    text = ""
