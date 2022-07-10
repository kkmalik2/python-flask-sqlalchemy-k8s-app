from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import inspect
import sys


Base = declarative_base()
# engine = create_engine('sqlite:///user-pref.db', echo = True)
engine = create_engine('sqlite:///user-pref.db', echo = True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind = engine)
session = Session()

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

# result = session.query(User).join(UserResponse).all()
# for i in range(0,len(result)):
#     for response in result[i].user_responses:
#         print (result[i])
#         print (result[i].name, response.favorite_actor)

# result = session.query(User).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
# print (result)
# for i in result:
#     print ("inside for loop")
#     print (type(i))
#     print (i.name)
#     # print (i.name, i.phone, i.user_responses.favorite_actor, i.user_responses.response_time)

result = session.query(User, UserResponse).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
for u, ur in result:
    print (u.name, ur.favorite_actor, ur.response_time)