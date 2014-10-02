#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("01: SQLAlchemy - Engine Basics")

#Actual tutorial begins here. For use with an interactive

from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db")
