#!/usr/bin/python3
'''This script list all `State` objects from the database'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if (__name__ == "__main__"):
    if (len(sys.argv) <= 3):
        exit()

    string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(string, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city_dict = {}
    id_list = []
    for obj in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(obj.id, obj.name, obj.state.name))
