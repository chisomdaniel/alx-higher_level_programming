#!/usr/bin/python3
'''This script prints the State object with the name passed as argument'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if (__name__ == "__main__"):
    if (len(sys.argv) <= 4):
        exit()

    string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(string, pool_pre_ping=True)

    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name==sys.argv[4]):
        print("{}".format(instance.id))
        exit()

    print("Not found")
