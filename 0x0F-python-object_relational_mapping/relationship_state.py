#!/usr/bin/python3
"""Module that defines the State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

# Create the base class for the declarative models
Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
    id (sqlalchemy.Column): The city's id.
    name (sqllchemy.Column): The city's name.
    state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Define he relatinship between State and City models
    cities = relationship("City",backref="states", cascade="all, delete")
