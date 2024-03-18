#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State.name, City.id, City.name).join(City).\
        order_by(City.id).all()

    for row in rows:
        state, city_id, city = row
        print("{}: ({}) {}".format(state, city_id, city))
