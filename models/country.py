from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from models.user import *

class CountryModel(Base):
  __tablename__ = 'countries'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)

  user = relationship("UserModel", back_populates="country")