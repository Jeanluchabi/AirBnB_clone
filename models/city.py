#!/usr/bin/python3
"""Defines a city class ."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city.

    Attributes:
        state_id (str): The idof the state .
        name (str): The city's name.
    """
    state_id = ""
    name = ""
