#!/usr/bin/python3
"""This module is for retreiving and printing all states froom a MSql database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm inport sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the  provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create a session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Search for the specified state in database
    state = session.query(State).filter_by(id=2).first()
    # Update the new statete to session
    state.name = "New Mexico"
    # Commit the session to persist the changes
    session.commit()
    # Print the ID of the newly added state
