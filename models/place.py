#!/usr/bin/python3
""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Representation of Place """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = places
        city_id = Column(String(60),
                         nullable=False)
        user_id = Column(String(60),
                         nullable=False)
        name = Column(String(128),
                      nullable=False)
        description = Column(String(1024),
                             nullable=False)
        number_rooms = Column(Integer,
                              default=0,
                              nullable=False)
        number_bathrooms = Column(Integer,
                                  default=0,
                                  nullable=False)
        max_guest = Column(Integer,
                           default=0,
                           nullable=False)
        price_by_night = Column(Integer,
                                default=0,
                                nullable=False)
        latitude = Float(Float,
                         nullable=False)
        longitude = Float(Float,
                         nullable=False)
        reviews = relationship("Review",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False,
                                 backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute that returns list of Review instances"""
        values_review = models.storage.all("Review").values()
        list_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review
