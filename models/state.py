#!/usr/bin/python3
"""Defines a class state."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state.

    Attribute:
        name (str): The state name.
    """
    name = ""
