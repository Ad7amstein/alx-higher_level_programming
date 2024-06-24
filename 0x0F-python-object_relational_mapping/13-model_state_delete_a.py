#!/usr/bin/python3
"""Delete states"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    removed_states = session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id).all()
    for state in removed_states:
        session.delete(state)
    session.commit()
    session.close()
