#!/usr/bin/python3
'''Connecting python to DATABASE using SQLALchemy'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence


Base = declarative_base()


class State(Base):
    '''A class for our state table'''

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
