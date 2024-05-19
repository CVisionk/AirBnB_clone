#!/usr/bin/env python3
""""
File to handle storage system of applications.
"""
import json
from models.base_model import BaseModel


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

    def reload(self):
        """
        Attempts to deserialize objects from JSON and load
        them into storage.
        """
        try:
            with open(self.__file_path, "r") as f:
                objects_dict = json.load(f)
                self.__objects = {
                    key: BaseModel(**value)
                    for key, value in objects_dict.items()
                }
        except FileNotFoundError:
            pass  # No action if file doesn't exist
