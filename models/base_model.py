#!/usr/bin/env python3
import uuid
import models
from datetime import datetime


class BaseModel():
    """
    Base class for all models in the application.

    Provides common attributes (id, created_at, updated_at) and methods
    for managing them.
    """
    def __init__(self, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
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
        models.storage.new(self)  # Register the object with storage
        models.storage.save()     # Persist all objects to the file

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        obj_dict = {
            'my_number': getattr(self, 'my_number', None),
            'name': getattr(self, 'name', None),
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
        return obj_dict
