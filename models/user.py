#!/usr/bin/python3
"""This module defines a class User"""
from lib2to3.pytree import Base
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base


storage_type = getenv("HBNB_TYPE_STORAGE")
Base = declarative_base()

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
