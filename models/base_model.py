#!/usr/bin/python3
from uuid import uuid4 as new_id
from datetime import datetime


class BaseModel():

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == "__class__":
                continue  # or pass
            elif key == "created_at" or key == "update_at":
                setattr(self, key, datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f"))
            else:
                setattr(self, key, value)
        else:
            self.id = str(new_id())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        """ self.name = name
        self.number = number
        self.id = str(new_id())
        self.current = datetime.now()
        self.update = self.current """

    def __str__(self):
        return ("[{}] ({}) <>".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict.update({"created_at": self.created_at.isoformat()})
        my_dict.update({"updated_at": self.updated_at.isoformat()})
        return my_dict


""" my_model = BaseModel()
my_other = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
print(my_other) """
