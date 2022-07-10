from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from .db_base import *

Base = get_base()

class User(Base):
   __tablename__ = 'users'
   __table_args__ = {'extend_existing': True} 

   id = Column(Integer, primary_key = True)
   name = Column(String)
   phone = Column(String)
   email = Column(String)
   address = Column(String)
   lastUpdateDate = Column(String)
   user_responses = relationship("UserResponse", back_populates = "user")

class UserResponse(Base):
    __tablename__ = 'users_responses'
    __table_args__ = {'extend_existing': True} 
    
    id = Column(Integer, primary_key = True)
    user_id = Column(String, ForeignKey('users.id'))
    favorite_actor = Column(String) 
    response_time = Column(String)
    user = relationship("User", back_populates = "user_responses")