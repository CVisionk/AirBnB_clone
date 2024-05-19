#!/usr/bin/env python3
"""
This file initializes the FileStorage system for the application.
It imports the FileStorage class and creates an instance to manage object
persistence using a file.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
