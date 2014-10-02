#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("01: SQLAlchemy - EXERCISE\n"
   "Assuming this table:\n\n"
   "CREATE TABLE employees {\n"
   "\temp_id INTEGER PRIMARY KEY,\n"
   "\temp_name VARCHAR(30)\n"
   "\t)\n\n"
   "And using the \"engine.execute()\" method, invoke a statement:\n"
   "1. Execute an INSERT statement that will insert the row with emp_name='dilbert'\n"
   "The primary key column can be omitted so that it is generated automatically.\n\n"
   "2. SELECT all rows from the employee table.\n")

#Begin exercise:
from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db", echo=True)
#As an employee already exists called "employees", we will be creating
#a table for  the office plants.
#engine.execute("CREATE TABLE contractors ("
#               "    cntr_id INTEGER PRIMARY KEY,"
#               "    cntr_name VARCHAR(30)"
#               ")")
engine.execute("INSERT INTO contractors(cntr_name) VALUES ('Alice')")
results = engine.execute("SELECT * FROM contractors")
