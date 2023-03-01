"""
This modules handles database connection and session creation aspects
of the app.

The SQLAlchemy Object Relational Mapper presents a method of associating
user-defined Python classes with database tables, and instances of those
classes (objects) with rows in their corresponding tables. It includes a
system that transparently synchronizes all changes in state between
objects and their related rows, called a unit of work, as well as a
system for expressing database queries in terms of the user defined
classes and their defined relationships between each other.

Links:
    https://fastapi.tiangolo.com/tutorial/sql-databases/#import-the-sqlalchemy-parts
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

# The return value of create_engine() is an instance of Engine, and it
# represents the core interface to the database, adapted through a
# dialect that handles the details of the database and DBAPI in use. In
# this case the SQLite dialect will interpret instructions to the Python
# built-in sqlite3 module.
# If we added 'echo=True' to the call, then all generated SQL would be
# outputed using Python's standard logging module.
# When using the ORM, we typically don’t use the Engine directly once
# created; instead, it’s used behind the scenes by the ORM as we’ll
# see shortly.
# See: https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls

# NOTE: "check_same_thread": False is needed only for SQLite. It's not
# needed for other databases. By default SQLite will only allow one
# thread to communicate with it, assuming that each thread would handle
# an independent request.
# This is to prevent accidentally sharing the same connection for 
# different things (for different requests).
# But in FastAPI, using normal functions (def) more than one thread
# could interact with the database for the same request, so we need
# to make SQLite know that it should allow that with 
# connect_args={"check_same_thread": False}.
# Also, we will make sure each request gets its own database
# connection session in a dependency, so there's no need for that
# default mechanism.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal is a class that creates session objects. 
# A Session is just a workspace for your objects, local to a particular
# database connection.
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session
# https://docs.sqlalchemy.org/en/20/orm/session_api.html

Base = declarative_base()
# Later we will inherit from this class to create each of the database
# models or classes (the ORM models):
# When using the ORM, the configurational process starts by describing
# the database tables we’ll be dealing with, and then by defining our
# own classes which will be mapped to those tables.
# Classes mapped using the Declarative system are defined in terms of
# a base class which maintains a catalog of classes and tables relative
# to that base - this is known as the declarative base class. Our
# application will usually have just one instance of this base in a
# commonly imported module. We create the base class using the 
# declarative_base() function, as done above.

def create_metadata():
    Base.metadata.drop_all(bind=engine)    # type: ignore
    Base.metadata.create_all(bind=engine)  # type: ignore
    # NOTE: Pylance doesn't recognize the 'metadata' attribute
