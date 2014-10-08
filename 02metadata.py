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

#echo enables logging of SQL statements:
#   engine = create_engine("sqlite:///some.db", echo=True)

# Code here has nothing to do with databases -- just Pythonic objects
metadata = MetaData() # Columns will populate themselves into this MetaData structure.
#Metadata() Serves as a place where relationshipscan be looked up 
user_table= Table('user', metadata, 
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('fullname', String)
              )
print('user_table.name =',user_table.name) #Retrieves name of table
print('user_table.c.name =',user_table.c.name) #.c is the Associative Array: kind of like a Py dict. 
print('user_table.c.keys() =',user_table.c.keys()) # All columns are accessible
print('user_table.c[\'id\'] =',user_table.c['id']) #Index specific columns

#Each column in .c. (like c.id or c.fullname) has its own attributes like
#type, name, eg:
print('user_table.c.id.name =',user_table.c.id.name)
print('user_table.c.id.type =', user_table.c.id.type)

print('user_table.primary_key =',user_table.primary_key) #Retrieves list of primary keys

print(user_table.select()) #The SQL statement to select column. Also takes where:

print(user_table.select().where(user_table.c.fullname == 'Joe'))

#Interface with Engine
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
metadata.create_all(engine)
