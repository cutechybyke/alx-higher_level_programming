#!/usr/bin/python3
"""This module is for retreiving and printing all states froom a MSql database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm inport sessionmaker
from model_state import State
from relationship_city import City

if __name__ == "__main__":

    #Get the command-line argumnts
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the SQLAlchemy engine using the  provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(mysql_username, mysql_password, database_name))

    # Create the database tables based on the defined model
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve and print the states and their cities
    cities = session.query(City).join(State).order_by(City.id)
        
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # close the session
    session.close()
