#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, Integer, String,\
        relationship
from os import getenv


class State(BaseModel, Base):
    """Defines the State class of the HBNB project"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state",
                          cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        from models import storage
        from models.city import City

        @property
        def cities(self):
            """propery decorator for cities attribute"""

            city_inst = storage.all(City)
            match_cities = []
            for key, obj in city_inst.items():
                if self.id == obj.state_id:
                    match_cities.append(obj)
            return match_cities
