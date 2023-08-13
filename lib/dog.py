from models import Dog

from sqlalchemy import (create_engine, Column, Integer, String, Index)
from sqlalchemy.ext.declarative import declarative_base
# To create a session, we need to use SQLAlchemy's sessionmaker class. This ensures that there is a consistent identity map for the duration of our session.
from sqlalchemy.orm import sessionmaker
# Inheritance from a declarative_base object.
Base = declarative_base()


class Dog(Base):
    # A __tablename__ class attribute.
    __tablename__ = 'dogs'
    Index('index_name', 'name')
    # A Column specified to be the table's primary key.
    # One or more Columns as class attributes.
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"\n Dog {self.id}: "\
            + f"{self.name} "\
            + f"Breed: {self.breed}"


def create_table(session, base):
    engine = create_engine('sqlite:///lib/dogs.db')
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    dogs = session.query(Dog).filter(Dog.name == name).first()
    return dogs
    
def find_by_id(session, id):
    dogs = session.query(Dog).filter(Dog.id == id).first()
    return dogs

def find_by_name_and_breed(session, name, breed):
    dogs = session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
    return dogs

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()