#!/usr/bin/python3
"""HThis module is for retreiving and printing all states froom a MSql database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm inport sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the  provided MySQL credentials
    engine = create_engine("mysql+mysqldb://():()@localhost/()".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create a session 
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve all states from the database
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
