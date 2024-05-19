#!/usr/bin/python3
'''handle sqlalchemy stuff'''
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review, 'Amenity': Amenity}


class DBStorage:
    '''handle sqlalchemy stuff'''
    __engine = None
    __session = None

    def __init__(self):
        '''makes engine'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''returns all objs'''
        obj_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                obj_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        '''adds object'''
        self.__session.add(obj)

    def save(self):
        '''commits current state'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete obj'''
        if obj:
            cls_name = all_classes[type(obj).__name__]

            self.__session.query(cls_name).\
                filter(cls_name.id == obj.id).delete()

    def reload(self):
        '''make session'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        '''close session'''
        self.__session.remove()
