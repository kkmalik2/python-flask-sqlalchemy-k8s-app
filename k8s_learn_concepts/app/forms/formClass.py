from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

def set_secret_key(app):
    # Flask-WTF requires an encryption key - the string can be anything
    app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

def bootstrap_app(app):
    # Flask-Bootstrap requires this line
    Bootstrap(app)

class NameForm(FlaskForm):
    user_name = StringField ("Enter Your Name: ")
    user_phone = IntegerField("Enter Your Phone #: ", validators=[DataRequired()])
    user_email = StringField ("Enter Your Email: ")
    user_address = StringField ("Enter Your Address: ")
    actor_name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')