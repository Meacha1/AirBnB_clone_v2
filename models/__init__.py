#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
import sys
sys.path.append("/AirBnB_clone_v2/models/engine/")

from db_storage import DBStorage
from file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()
