import datetime
from  sqlalchemy import (Column, Integer, Text, DateTime, ForeignKey,
                         create_engine, Boolean, String)
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app.sqlite', echo=True)
Base = declarative_base(bind=engine)

class Abstract(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.datetime.now())

class User(Base, Abstract):
    __tablename__= 'users'
    name = Column(String(30), unque=True, nullable=False)
    name = Column(String(40), unque=True, nullable=False)
    password = Column(String(100), nullable=False)

    user_links = relationship('Link')

    def __str__(self):
        return '  |  '.join(self.name, self.email, self.password)