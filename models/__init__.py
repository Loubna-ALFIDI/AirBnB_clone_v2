#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
#from models.engine.db_storage import DBStorage
#from os import getenv


#storage_type = getenv('HBNB_TYPE_STORAGE')
#if storage_type == 'db':
#    storage = DBStorage()
#else:
#    storage = FileStorage()
#storage.reload()
