#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os
from models.base_model import BaseModel


class FileStorage:
     """Serializes instances to a JSON file and deserializes JSON file to instances."""

     __file_path = "file.json"
     __objects = {}

     def all(self):
          """Return dictionary object"""
          return FileStorage.__objects

     def new(self, obj):
          """Sets in __objects the obj with key <obj class name>.id."""
          key = f"{obj.__class__.__name__}.{obj.id}"
          FileStorage.__objects[key] = obj

     def save(self):
          """serializes __objects to the JSON file (path: __file_path)"""
          obj_dict = {}
          for key, obj in FileStorage.__objects.items():
               obj_dict[key] = obj.__dict__
          with open(FileStorage.__file_path, 'w') as File:
               json.dump(obj_dict, File)

     def reload(self):
          """deserializes the JSON file to __objects"""
          if os.path.exists(FileStorage.__file_path):
               with open(FileStorage.__file_path, 'r') as File:
                    obj_dict = json.load(File)
                    for key, value in obj_dict.items():
                         class_name, obj_id = key.split('.')
                         obj_instance = globals()[class_name](**value)
                         FileStorage__objects[key] = obj_instance
