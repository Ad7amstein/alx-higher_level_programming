#!/usr/bin/python3
"""Contains 'a'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)

    for instance in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id):
        print(f"{instance.id}: {instance.name}")
