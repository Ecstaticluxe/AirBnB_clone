#!/usr/bin/python3
"""This defines the base model"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class where all other classes inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance

        Args:
            - *args: list of arguments
            - *kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel."""
        return "[{}] ({}) {}"
    .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] =
        self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        obj_dict['updated_at'] =
        self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        return obj_dict
