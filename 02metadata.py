#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("02: SQLAlchemy - Schema and Metadata")

#Actual tutorial begins here. For use with an interactive

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String

#echo enables logging of SQL statements
#engine = create_engine("sqlite:///some.db", echo=True)

metadata = MetaData()
user_table= Table('user', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('fullname', String)
                  )
