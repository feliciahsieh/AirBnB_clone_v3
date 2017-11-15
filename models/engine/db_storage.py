#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with a mysql+mysqldb database
connection.
"""

import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if not self.__session:
            self.reload()
        objects = {}
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session.query(Amenity):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
            for obj in self.__session.query(City):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
            for obj in self.__session.query(Place):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
            for obj in self.__session.query(State):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
            for obj in self.__session.query(Review):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
            for obj in self.__session.query(User):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj

        return objects

    def reload(self):
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
        Base.metadata.create_all(self.__engine)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)
