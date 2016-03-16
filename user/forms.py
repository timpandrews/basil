from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class SignupForm(Form):
    fullname = StringField('Full Name', [validators.Required()])
    email =EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=8, max=60)
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=8, max=60)
    ])