#!/usr/bin/python3
"""This module is for retreiving and printing all states froom a MSql database"""
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

    # Search for the specified state in database
    found = False
    for state in session.query(State)
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    # Print a message if state not found
    if found is False:
        print("Not found")
