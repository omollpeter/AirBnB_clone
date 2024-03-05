#!/usr/bin/python3
"""
This module is used to create a unique FileStorage instance for the
application

Variables:
    storage: Instance of FileStorage
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
