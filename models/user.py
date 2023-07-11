from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from models.country import CountryModel
from models.book import BookModel

class UserModel(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  password = Column(String)
  role = Column(String)
  country_id = Column(Integer, ForeignKey('countries.id'))

  country = relationship("CountryModel", back_populates="user")
  books=relationship('BookModel', back_populates='user')