from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Next')
    number = IntegerField()
    td = HiddenField()