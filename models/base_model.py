import models
import uuid
from datetime import datetime

"""Defining class BaseModel"""


class BaseModel:
    """Represents Base Model of the project"""

    def __init__(self, *args, **kwargs):
        """initialize base model
        Args:
        *args: non used
        **kwargs: key/value pair of attributes
        """
        formatt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, formatt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """print representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saving the time when obj updated"""
        self.created_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
