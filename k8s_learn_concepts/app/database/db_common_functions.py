from sqlalchemy import inspect
from datetime import datetime
from .db_classes import *
from .db_engine import *

engine = create_db_engine()
session = create_session(engine)


def create_metadata():
    Base.metadata.create_all(engine)
    print ("Metadata created ")

def cleanup_tables():
    if inspect(engine).has_table('users'): 
        User.__table__.drop(engine)
    if inspect(engine).has_table('users_responses'):
        UserResponse.__table__.drop(engine)

def drop_table(class_name):
    # print ("Variable Type: ")
    # print  (type(class_name))
    if class_name == 'User':
        User.__table__.drop(engine)
    if class_name == 'UserResponse':
        UserResponse.__table__.drop(engine)

def insert_user(name, phone, email, address):
    now = datetime.now()
    result = session.query(User).filter(User.phone == phone).all()
    result_length = len(result)
    if result_length == 0:
        c1 = User(name = name, phone = phone, email = email, address = address, lastUpdateDate=now)
        session.add(c1)
    else:
        print ("printing result...")
        print (result)
        user_id = result[0].id
        session.query(User).filter(User.id == user_id).  \
        update({User.name : name, User.email : email, User.address : address, User.lastUpdateDate : now}, synchronize_session = False)
    session.commit()

def insert_user_response(name, phone, email, address, actor_name):
    now = datetime.now()
    result = session.query(User).filter(User.phone == phone).all()
    print ("printing result. user response..")
    print (result[0])
    user_id = result[0].id
    c1 = UserResponse(user_id = user_id, favorite_actor = actor_name, response_time = now)
    session.add(c1)
    session.commit()

def show_users():
    # print ("Recursion limit : ")
    # print(sys.getrecursionlimit())
    if inspect(engine).has_table('users'):
        result = session.query(User).order_by(User.lastUpdateDate).all()
        return result
    else:
        print ("Table does not exist")
        return []

def show_users_response():
    if inspect(engine).has_table('users'):
        # result = session.query(User).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
        result = session.query(User, UserResponse).join(UserResponse).order_by(UserResponse.response_time.desc()).all()
        return result
    else:
        print ("Table does not exist")
        return []

def session_close(session):
    session.close()