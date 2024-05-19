#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    '''hbnb clone state class'''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            '''cities getter'''
            from models import storage
            from models.city import City
            city_dicts = storage.all(City)
            city_list = []

            for c in city_dicts.values():
                if c.state_id == self.id:
                    city_list.append(c)

            return city_list
