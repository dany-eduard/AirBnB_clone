#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class menages the information of a user object """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
