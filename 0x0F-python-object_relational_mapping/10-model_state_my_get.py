#!/usr/bin/python3
"""This script prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy.exc import NoResultFound

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = argv[4]

    try:
        query = session.query(State.id)\
                              .filter(State.name.like(text(':state_name')))\
                              .params(state_name=state_name)
        num = query.one()
        for value in num:
            print(value)
    except NoResultFound:
        print('Not found')
