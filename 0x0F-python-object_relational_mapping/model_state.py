#!/usr/bin/python3
"""This file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    """A State class that defines a Table `states` and its Columns"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
