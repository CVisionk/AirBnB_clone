#!/usr/bin/env python3
"""
Base files for all models in the application.
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel():
    """
    Base class for all models in the application.

    Provides common attributes (id, created_at, updated_at) and methods
    for managing them.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            args: list of arguments
            kwargs (dict, optional): A dictionary of keyword arguments
                corresponding to the object's attributes.
                - If provided, sets attributes based on key-value pairs.
                - If not provided, generates a new UUID for id,
                  sets created_at and updated_at to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns:
                 a string representation of the object in a
                 human-readable format.
                 Includes the class name, object ID, and all
                 its attributes.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
        Saves the current object's state to the
        persistent storage system.
        """
        self.updated_at = datetime.now()
        """Saves the current object to storage."""
        storage.save()     # Persist all objects to the file

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
