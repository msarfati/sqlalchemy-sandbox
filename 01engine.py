#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
print("01: SQLAlchemy - Engine Basics")

from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db")
