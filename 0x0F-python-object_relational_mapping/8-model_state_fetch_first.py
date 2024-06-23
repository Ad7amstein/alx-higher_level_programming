#!/usr/bin/python3
"""First state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)
    first_state = session.query(State).order_by(State.id).first()
    if (first_state is None):
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
