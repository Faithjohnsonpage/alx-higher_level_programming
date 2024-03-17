#!/usr/bin/python3
"""This script prints the first State object
from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.id, State.name).order_by(State.id)

    # Execute the query to fetch results
    row = query.first()

    if row:
        print("{}: {}".format(row.id, row.name))
