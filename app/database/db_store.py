# # from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
# # from .db_engine import *
# # from db_engine import *
# from .db_engine import *
# from .db_base import *
# from .db_classes import *

# from datetime import datetime

# import sys


# Base = get_base()
# # engine = create_engine('sqlite:///user-pref.db', echo = True)
# # engine = create_engine('sqlite:///user-pref.db', echo = True, connect_args={'check_same_thread': False})
# engine = create_db_engine()
# session = create_session(engine)
# # Session = sessionmaker(bind = engine)
# # session = Session()


# # User.user_responses = relationship("users_responses", order_by = UserResponse.id, back_populates = "users")

# def drop_table(class_name):
#     # print ("Variable Type: ")
#     # print  (type(class_name))
#     if class_name == 'User':
#         User.__table__.drop(engine)
#     if class_name == 'UserResponse':
#         UserResponse.__table__.drop(engine)

# def cleanup_tables():
#     if inspect(engine).has_table('users'): 
#         User.__table__.drop(engine)
#     if inspect(engine).has_table('users_responses'):
#         UserResponse.__table__.drop(engine)

# def create_metadata():
#     Base.metadata.create_all(engine)
#     print ("Metadata created ")




# def session_close():
#     session.close()

# def test_func():
#     print ("This is test for shared functions !!")

# def show_users():
#     # print ("Recursion limit : ")
#     # print(sys.getrecursionlimit())
#     if inspect(engine).has_table('users'):
#         result = session.query(User).order_by(User.lastUpdateDate).all()
#         return result
#     else:
#         print ("Table does not exist")
#         return []
#     # print (type(result))
#     # for r in result:
#         # print (r.name, r.phone)
#     # return result
# # show_users()

# def show_users_response():
#     if inspect(engine).has_table('users'):
#         # result = session.query(User).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
#         result = session.query(User, UserResponse).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
#         return result
#     else:
#         print ("Table does not exist")
#         return []
