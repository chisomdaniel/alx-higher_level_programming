#!/usr/bin/python3
'''This script list all `State` objects from the database'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if (len(sys.argv) <= 3 or __name__ != "__main__"):
    exit()

string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(string, pool_pre_ping=True)

# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(State).order_by(State.id):
    print("{}: {}".format(instance.id, instance.name))
