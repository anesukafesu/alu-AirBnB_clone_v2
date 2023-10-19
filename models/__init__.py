#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ

storage_type = environ['HBNB_TYPE_STORAGE']
storage = None

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

print(storage)
storage.reload()
