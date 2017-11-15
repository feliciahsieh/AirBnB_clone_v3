#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel


class State(BaseModel, Base):
    """Representation of state """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        city = relationship("City",
                            backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """fs getter attribute that returns City instances"""
        values_city = models.storage.all("City").values
        list_city = []
        for city in values_city:
            if city.state_id == self.id:
                list_city.append(city)
        return list_city
