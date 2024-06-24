#!/usr/bin/python3
"""Update a state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys
from sqlalchemy.orm.exc import NoResultFound


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    try:
        state = session.query(State).filter_by(id=2).one()
        state.name = "New Mexico"
    except NoResultFound:
        pass
    session.commit()
    session.close()
