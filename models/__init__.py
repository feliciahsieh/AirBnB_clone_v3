#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from base_model import Base, BaseModel
from amenity import Amenity
from city import City
from place import Place
from review import Review
from state import State
from user import User

"""DBSTORAGE"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
"""FILESTORAGE"""
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
