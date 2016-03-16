from basil import app
from flask import render_template, redirect, url_for, session, request
from user.forms import SignupForm
from user.decorators import login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')