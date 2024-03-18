#!/usr/bin/python3
"""This file that contains the class definition of a City"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """A City class that defines a Table `cities` and its Columns"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
