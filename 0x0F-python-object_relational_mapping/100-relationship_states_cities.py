#!/usr/bin/python3
"""This module is for retreiving and printing all states froom a MSql database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm inport sessionmaker
from model_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the  provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create the database tables based on the defined models
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new city
    session.add(City(name="San Francisco", state=State(name="California")))
    # Commit the session to persist the changes
    session.commit()
