#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("02: SQLAlchemy - Schema and Metadata")

#Actual tutorial begins here. For use with an interactive

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Enum
from sqlalchemy import ForeignKey

#echo enables logging of SQL statements:
#   engine = create_engine("sqlite:///some.db", echo=True)

# Code here has nothing to do with databases -- just Pythonic objects
metadata = MetaData() # Columns will populate themselves into this MetaData structure.
#Metadata() Serves as a place where relationshipscan be looked up 
fancy_table= Table('fancy', metadata, 
                  Column('key', String(50), primary_key=True),
                  Column('timestamp', DateTime),
                  Column('type', Enum('a', 'b', 'c'))
                   )

address_table = Table('address', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('email_address', String(100), nullable=False),
                      Column('user_id', Integer, ForeignKey('user.id'))
                      )

#Interface with Engine
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
metadata.create_all(engine)
address_table.create(engine)
