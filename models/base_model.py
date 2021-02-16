#!/usr/bin/python3
"""
Creating a class call BaseModel
"""
import models
from uuid import uuid4 as new_id
from datetime import datetime


class BaseModel():
    def __init__(self, *args, **kwargs):
        """ Function That Initialize The Class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # or pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(new_id())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Function That Return a string about the Instance """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Function that Update the attribute update_at with the current
        time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of
        the instance """
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict.update({"created_at": self.created_at.isoformat()})
        my_dict.update({"updated_at": self.updated_at.isoformat()})
        return my_dict
