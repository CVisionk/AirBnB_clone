#!/usr/bin/env python3
""""
File to handle storage system of applications.
"""
import json
#from models.base_model import BaseModel


class FileStorage:
    """A class to handle file-based storage of objects."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects keyed by "<class name>.id"

    def all(self):
        """Returns the dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON and writes them to the file."""
        objects_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)
    
    def classList(self):
        """
        returns classlist of storable objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list ={
            "BaseModel" : BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        return class_list

    def reload(self):
        """
        Attempts to deserialize objects from JSON and load
        them into storage.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classList()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                # overwrite or insert?
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass  # No action if file doesn't exist
