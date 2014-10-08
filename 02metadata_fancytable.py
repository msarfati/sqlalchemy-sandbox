#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("02: SQLAlchemy - Schema and Metadata")

# Actual tutorial begins here. For use with an interactive

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Unicode, UnicodeText, Integer, String, DateTime, Enum
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)

# echo enables logging of SQL statements:
#   engine = create_engine("sqlite:///some.db", echo=True)

# Code here has nothing to do with databases -- just Pythonic objects
metadata = MetaData() # Columns will populate themselves into this MetaData structure.
# Metadata() Serves as a place where relationships can be looked up 
metadata.create_all(engine)
user_table= Table('user', metadata, 
                  Column('id', Integer, ForeignKey('address.id'), primary_key=True),
                  Column('name', String),
                  Column('fullname', String)
                )
fancy_table= Table('fancy', metadata, 
                  Column('key', String(50), primary_key=True),
                  Column('timestamp', DateTime),
                  Column('type', Enum('a', 'b', 'c'))
                )

address_table = Table('address', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email_address', String(100), nullable=False),
                  Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
                )
# Order of table creation matters for PK/FK constraints. In above example, if we
# create the user_table first, and it can references bogus, the commit will still go through,
# But, because address_table is created later, it must be able to reference the first user_table

story_table = Table('story', metadata,
                    Column('story_id', Integer, primary_key=True),
                    Column('version_id', Integer, primary_key=True),
                    Column('headline', Unicode(100), nullable=False),
                    Column('body', UnicodeText),
                    )

published_table = Table('published', metadata,
                        Column('pub_id', Integer, primary_key=True),
                        Column('pub_timestamp', DateTime, nullable=False),
                        Column('story_id', Integer),
                        Column('version_id', Integer),
                        ForeignKeyConstraint(
                            ['story_id', 'version_id'],
                            ['story.story_id', 'story.version_id'],
                            )
                        )
                        

# Interface with Engine
fancy_table.create(engine)
address_table.create(engine)
