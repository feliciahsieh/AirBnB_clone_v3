#!/usr/bin/python3
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
import os
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy import relationship
from sqlalchemy import ForeignKey

class Review(BaseModel, Base):
    """Representation of Review """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = reviews
        text = Column(String(1024),
                      nullable=False)
        place_id = Column(String(60),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
