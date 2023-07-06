from db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

class StateModel(Base):
  __tablename__ = 'states'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)