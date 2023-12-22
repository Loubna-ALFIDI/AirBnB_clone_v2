#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all,delete")

    @property
    def cities(self):
        """ Getter attribute to retrieve a list of cities"""
        from models import storage

        city_list = []
        for city_id, city_list in storage.all(City).items():
            if city_list.state_id == self.id:
                city_list.append(city_list)
        return city_list
