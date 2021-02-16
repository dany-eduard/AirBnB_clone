#!/usr/bin/python3
""" Class Review  """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class menages the information for a review objetc """
    place_id = ""
    user_id = ""
    text = ""
