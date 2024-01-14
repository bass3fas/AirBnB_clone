#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines Class User inherited from BaseModel"""


class User(BaseModel):
    """defining class user and it's attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
