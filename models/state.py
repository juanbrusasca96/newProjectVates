from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from models.book import *

class StateModel(Base):
  __tablename__ = 'states'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  
  books=relationship('BookModel', back_populates='state')