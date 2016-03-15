from basil import app
from flask import render_template, redirect
from user.forms import SignupForm
from user.models import User

@app.route('/login')
def login():
    return render_template('user/login.html')

@app.route('/signup', methods=('GET','POST'))
def signup():
    form = SignupForm()
    return render_template('user/signup.html', form=form)