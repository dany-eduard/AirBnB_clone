#!/usr/bin/python3
"""
FileStorage Class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStoreage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objets"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """  deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, "r") as f:
                my_dict = json.loads(f.read())
            for key, value in my_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name + '(**value)')
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
