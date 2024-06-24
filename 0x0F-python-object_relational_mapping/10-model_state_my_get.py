#!/usr/bin/python3
"""Get a state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy.orm.exc import NoResultFound
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state_name = sys.argv[4]
    session = Session(bind=engine)
    try:
        state = session.query(State).filter_by(name=state_name).one()
        print(state.id)
    except NoResultFound:
        print("Not found")
    session.close()
