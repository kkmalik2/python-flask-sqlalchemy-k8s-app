import os

print('*----------------------------------*')
print(os.environ)

database_type = os.getenv('DATABASE_TYPE')
database_location = os.getenv('DATABASE_LOCATION')
print (database_type)
print (database_location)
# engine = create_engine(f'{database_type}:///{database_location}', echo = True, connect_args={'check_same_thread': False})
# engine = create_engine('sqlite:///user-pref.db', echo = True, connect_args={'check_same_thread': False})
