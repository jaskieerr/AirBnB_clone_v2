#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column , String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''user update'''
    __tablename__ = "users"
    email = Column(String(128), null=False)
    password = Column(String(128), null=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", owner_bref="user", del_cascade="delete")
    reviews = relationship("Review", owner_bref="user", del_cascade="delete")
