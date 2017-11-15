#!/usr/bin/python3
"""
initialize the models package
"""

import os

"""DBSTORAGE"""
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
"""FILESTORAGE"""
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
