from basil import app
from flask import render_template, redirect
from user.forms import RegisterForm

@app.route('/login')
def login():
    return 'Hello User!'

@app.route('/register', methods=('GET','POST'))
def register():
    form = RegisterForm()
    return render_template('author/register.html', form=form)