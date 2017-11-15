#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import ForeignKey

class City(BaseModel):
    """Representation of city """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
