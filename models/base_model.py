#!/usr/bin/python3
from uuid import uuid4 as new_id
import datetime
class BaseModel():

    def __init__(self, name = None, number = None ):
        self.name = name
        self.number = number
        self.id = str(new_id())
        self.current = datetime.datetime.now()
        self.update = self.current

    def __str__(self):
        return ("[{}] ({}) <>".
                format(self.__class__.__name__, self.id ))

my_model = BaseModel()
my_other = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
print(my_other)


