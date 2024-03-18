#!/usr/bin/python3
"""This script prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    new_state = State(name='Louisiana')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new_state to the session
    session.add(new_state)

    # Commit changes to the database
    session.commit()
    new_state_id = session.query(State.id).\
        filter(State.name == 'Louisiana').scalar()

    print(new_state_id)
