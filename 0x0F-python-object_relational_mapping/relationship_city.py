#!/usr/bin/python3
'''Connecting python to DATABASE using SQLALchemy'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from relationship_state import Base, State
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''A class for our city table'''

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
