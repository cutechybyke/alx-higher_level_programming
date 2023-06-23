#!/usr/bin/python3
"""This module is for retreiving and printing all states froom a MSql database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm inport sessionmaker
from model_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the  provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create the database tables based on the defined model
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve and print the states and their cities
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("   {}: {}".format(city.id, city.name))
