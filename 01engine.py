#!/usr/bin/env python
# Michael Sarfati -- tutorial from Mike Bayer's Introduction to SQLAlchemy
# ( https://www.youtube.com/watch?v=P141KRbxVKc )
# This script explores SQL alchemy's engine basics
from lessonNice import printBorder as pb
pb("01: SQLAlchemy - Engine Basics")

#Actual tutorial begins here. For use with an interactive

from sqlalchemy import create_engine

#echo enables logging of SQL statements
engine = create_engine("sqlite:///some.db", echo=True)
print("Engine = ", engine)
#Result here acts like a cursor, and just interacts with the data.
result = engine.execute(
    "SELECT * FROM employees")

row = result.fetchone()
'''Result (which is really just a cursor) will close
implicitly, once the result has been placed into a variable,
or printed to the screen. But you an also close it explicitly like this.'''
result.close()
#print(result.fetchall())

conn = engine.connect()
trans = conn.begin()
#conn.execute("INSERT INTO employees "
             #"(emp_name) VALUES (:emp_name)", emp_name="Xena Xenos")
conn.execute(
    "UPDATE employees SET emp_wage = :emp_wage WHERE emp_name='Xena Xenos'", emp_wage=21.15)
trans.commit()
conn.close()

#Using with to connect, and right-away execute a statement
with engine.begin() as conn:
    conn.execute("SELECT * FROM employees")
