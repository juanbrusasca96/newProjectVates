from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from models.user import *
from models.state import StateModel

class BookModel(Base):
  __tablename__ = 'books'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)
  user_id=Column(Integer, ForeignKey('users.id'))
  state_id=Column(Integer, ForeignKey('states.id'))
  
  user=relationship('UserModel', back_populates='books')
  state=relationship('StateModel', back_populates='books')