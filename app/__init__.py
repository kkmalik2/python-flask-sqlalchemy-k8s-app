# from cgitb import reset
from time import asctime
from flask import Flask
from flask import render_template, url_for, redirect
from app.database.db_common_functions import *
from app.forms.formClass import *
# from datetime import datetime
import logging
logging.basicConfig(filename='app.log', filemode='a+', format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
set_secret_key(app)

# Required for Flask-bootstrap
bootstrap_app(app)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('home_page.html',title='HomePage')

@app.route('/fill-form', methods=['GET','POST'])
def form_fill_page():
    # logger.info("Form Fill")
    logger.info("This is an info message !!!")
    # cleanup_tables()
    form=NameForm()
    # message = ""
    if form.validate_on_submit():
        user_name = form.user_name.data
        user_phone = form.user_phone.data
        user_email = form.user_email.data
        user_address = form.user_address.data
        actor_name=form.actor_name.data
        # return redirect('actor.html',name=name)
        # test_func()
        # drop_table('User')
        create_metadata()
        insert_user(user_name, user_phone, user_email, user_address)
        insert_user_response(user_name, user_phone, user_email, user_address, actor_name)
        return render_template('actor.html', user_name=user_name, actor_name = actor_name)
    return render_template('render_form.html',title='HomePage', form = form)


@app.route('/user')
def hello_kanishk():
    user = {'username':'Kanishk'}
    return render_template('user_welcome.html',title='kk', user=user)
    # return "Hello Kanishk !!"

# @app.route('/user/<string:Name>')
# def hello_user(Name):
#     user = {'username': Name}
#     return render_template('user_welcome.html',title='kk', user=user)

@app.route('/show-user')
def show_user_list():
    result = show_users()
    len_result = len(result)
    print (type(result))
    print (len(result))
    # print (result)
    return render_template('show_users.html',title='kk', len_result = len_result, result = result)

@app.route('/show-user-response')
def show_user_response_list():
    result = show_users_response()
    len_result = len(result)
    return render_template('show_users_response.html',title='kk', len_result = len_result, result = result)


