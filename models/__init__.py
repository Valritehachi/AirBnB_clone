#!/usr/bin/python3
"""this is a magic method for models directory with storage."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
